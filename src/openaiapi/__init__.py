import os

from apiron import JsonEndpoint, Service


class OpenAI(Service):
    """Wrapper class around the OpenAI API"""

    domain = "https://api.openai.com"

    completions = JsonEndpoint(path="/v1/completions", default_method="POST")

    edits = JsonEndpoint(path="/v1/edits", default_method="POST")

    embeddings = JsonEndpoint(path="/v1/embeddings", default_method="POST")

    files = JsonEndpoint(path="/v1/files")
    file = JsonEndpoint(path="/v1/files/{file_id}")
    file_content = JsonEndpoint(path="/v1/files/{file_id}/content")

    fine_tunes = JsonEndpoint(path="/v1/fine-tunes")
    fine_tune = JsonEndpoint(path="/v1/fine-tunes/{fine_tune_id}")
    fine_tune_cancel = JsonEndpoint(path="/v1/fine-tunes/{fine_tune_id}/cancel", default_method="POST")
    fine_tune_events = JsonEndpoint(path="/v1/fine-tunes/{fine_tune_id}/events")

    image_generations = JsonEndpoint(path="/v1/images/generations", default_method="POST")
    image_edits = JsonEndpoint(path="/v1/images/edits", default_method="POST")
    image_variations = JsonEndpoint(path="/v1/images/variations", default_method="POST")

    models = JsonEndpoint(path="/v1/models")
    model = JsonEndpoint(path="/v1/models/{model}")

    moderations = JsonEndpoint(path="/v1/moderations", default_method="POST")

    @property
    def required_headers(self):
        """Required headers for API calls; these can be enhanced or overridden on a per-call basis."""

        openai_api_key = os.getenv("OPENAI_API_KEY", "XXXXXXXX")
        if openai_api_key == "XXXXXXXX":
            raise RuntimeError("No OpenAI API key found.")

        return {
            "Authorization": f"Bearer {openai_api_key}",
        }
