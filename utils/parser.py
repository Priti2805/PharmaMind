import re


def parse_salt_info(
        salt_text,
        brand_name
):

    result = {

        "API": "",
        "Strength": "",
        "Dosage Form": "",
        "Clean Brand Name": ""

    }

    try:

        apis = []
        strengths = []

        parts = salt_text.split(
            "+"
        )

        for part in parts:

            part = part.strip()

            match = re.search(
                r"(.+?)\s*\((.*?)\)",
                part
            )

            if match:

                apis.append(
                    match.group(1).strip()
                )

                strengths.append(
                    match.group(2).strip()
                )

            else:

                apis.append(
                    part
                )

        result["API"] = (
            " + ".join(
                apis
            )
        )

        result["Strength"] = (
            " + ".join(
                strengths
            )
        )

    except Exception:

        result["API"] = salt_text

    dosage_forms = [

        "Tablet",
        "Capsule",
        "Injection",
        "Syrup",
        "Suspension",
        "Cream",
        "Ointment",
        "Gel",
        "Lotion",
        "Drops",
        "Eye Drop",
        "Ear Drop",
        "Nasal Spray",
        "Spray",
        "Powder"

    ]

    try:

        for form in dosage_forms:

            if (
                form.lower()
                in brand_name.lower()
            ):

                result[
                    "Dosage Form"
                ] = form

                break

    except Exception:
        pass

    try:

        clean_name = brand_name

        for form in dosage_forms:

            clean_name = re.sub(
                form,
                "",
                clean_name,
                flags=re.IGNORECASE
            )

        result[
            "Clean Brand Name"
        ] = clean_name.strip()

    except Exception:

        result[
            "Clean Brand Name"
        ] = brand_name

    return result