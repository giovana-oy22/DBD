from time import sleep

from django.core.management.base import BaseCommand

from core.models import Cliente
from core.services.geocoding import geocode_address


class Command(BaseCommand):
    help = "Preenche coordenadas (latitude/longitude) de clientes com base no endereco cadastrado."

    def add_arguments(self, parser):
        parser.add_argument(
            "--force",
            action="store_true",
            help="Regeocodifica todos os clientes, inclusive os que ja possuem coordenadas.",
        )
        parser.add_argument(
            "--limit",
            type=int,
            default=0,
            help="Limita a quantidade de clientes processados (0 = sem limite).",
        )
        parser.add_argument(
            "--throttle",
            type=float,
            default=1.0,
            help="Intervalo em segundos entre requisicoes de geocodificacao.",
        )

    def handle(self, *args, **options):
        force = options["force"]
        limit = options["limit"]
        throttle = options["throttle"]

        if force:
            queryset = Cliente.objects.order_by("id")
        else:
            queryset = Cliente.objects.filter(latitude__isnull=True, longitude__isnull=True).order_by("id")

        if limit and limit > 0:
            queryset = queryset[:limit]

        total = queryset.count()
        if total == 0:
            self.stdout.write(self.style.WARNING("Nenhum cliente pendente para backfill."))
            return

        self.stdout.write(f"Iniciando backfill de {total} cliente(s)...")

        atualizados = 0
        falhas = 0

        for indice, cliente in enumerate(queryset, start=1):
            endereco = cliente.endereco_completo()
            coordenadas = geocode_address(endereco)

            if coordenadas:
                cliente.latitude, cliente.longitude = coordenadas
                cliente.save(update_fields=["latitude", "longitude"])
                atualizados += 1
                self.stdout.write(
                    self.style.SUCCESS(
                        f"[{indice}/{total}] OK cliente={cliente.id} lat={cliente.latitude:.6f} lon={cliente.longitude:.6f}"
                    )
                )
            else:
                falhas += 1
                self.stdout.write(
                    self.style.WARNING(
                        f"[{indice}/{total}] FALHA cliente={cliente.id} endereco={endereco}"
                    )
                )

            if throttle > 0 and indice < total:
                sleep(throttle)

        self.stdout.write("")
        self.stdout.write(self.style.SUCCESS(f"Backfill finalizado. Atualizados: {atualizados}"))
        self.stdout.write(self.style.WARNING(f"Falhas: {falhas}"))
