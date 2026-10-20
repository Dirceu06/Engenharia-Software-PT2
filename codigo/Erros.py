class ReservaError(Exception):
    """Erro base das regras de reserva."""


class HorarioInexistenteError(ReservaError):
    pass


class HorarioLotadoError(ReservaError):
    pass


class LimiteSemanalError(ReservaError):
    pass


class ReservaDuplicadaError(ReservaError):
    pass
