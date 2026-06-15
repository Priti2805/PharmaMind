class ManufacturerNormalizerAgent:

    def normalize(
        self,
        manufacturer
    ):

        if not manufacturer:

            return "Unknown"

        manufacturer = (
            manufacturer
            .lower()
            .replace(
                "pharmaceuticals limited",
                ""
            )
            .replace(
                "pharmaceuticals ltd",
                ""
            )
            .replace(
                "limited",
                ""
            )
            .replace(
                "ltd",
                ""
            )
            .replace(" ", "")
            .strip()
        )

        return manufacturer

    def run(
        self,
        manufacturer_summary
    ):

        normalized = {}

        for manufacturer, info in (
            manufacturer_summary.items()
        ):

            key = self.normalize(
                manufacturer
            )

            if key not in normalized:

                normalized[key] = {
                    "count": 0,
                    "products": []
                }

            normalized[key]["count"] += (
                info["count"]
            )

            normalized[key]["products"].extend(
                info["products"]
            )

        return normalized