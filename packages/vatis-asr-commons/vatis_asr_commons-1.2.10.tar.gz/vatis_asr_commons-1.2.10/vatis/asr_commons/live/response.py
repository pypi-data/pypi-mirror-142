import dataclasses


@dataclasses.dataclass
class ReservationResponse:
    token: str
    pod_name: str
    stream_url: str
