import base64
import json
from typing import Callable, Dict, Any, Optional, List


def build_jwt(
    header: Dict[str, Any],
    payload: Dict[str, Any],
    signer: Callable[[Any], Any]
) -> str:
    encoded_header = base64.urlsafe_b64encode(json.dumps(header).encode()).replace(b"=", b"")
    encoded_payload = base64.urlsafe_b64encode(json.dumps(payload).encode()).replace(b"=", b"")

    jwt_segments = [encoded_header, encoded_payload]

    signing_input = b".".join(jwt_segments)
    signature = signer(signing_input)
    encoded_signature = base64.urlsafe_b64encode(signature).replace(b"=", b"")
    jwt_segments.append(encoded_signature)

    return b".".join(jwt_segments).decode("utf-8")
