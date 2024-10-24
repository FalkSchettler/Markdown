import yaml
import sys


def main():
    try:
        # Read YAML file
        with open("traceability_report.yaml", "r") as file:
            report = yaml.safe_load(file)

        # Extract tested and untested requirements
        tested_requirements = report.get("tested_requirements", [])
        untested_requirements = report.get("untested_requirements", [])

        # List tested requirements
        print("Tested Requirements:")
        if tested_requirements:
            for req in tested_requirements:
                print(f"- {req}")
        else:
            print("None")

        # List untested requirements
        print("\nUntested Requirements:")
        if untested_requirements:
            for req in untested_requirements:
                print(f"- {req}")
        else:
            print("None")

        # Check if there are untested requirements
        if untested_requirements:
            print(f"\nThere are {len(untested_requirements)} untested requirements!")
            sys.exit(1)
        else:
            print("\nAll requirements are tested.")
            sys.exit(0)

    except FileNotFoundError:
        print("Error: traceability_report.yaml not found.")
        sys.exit(1)
    except yaml.YAMLError as e:
        print(f"Error parsing YAML: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
