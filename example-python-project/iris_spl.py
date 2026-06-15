# iris_spl.py
import sys
from iris_spl.core import IRISClient

def main():
    if len(sys.argv) < 2:
        print("Usage: python iris_spl.py \"Your investigation question\"")
        sys.exit(1)

    question = sys.argv[1]
    iris = IRISClient.from_config("config.yaml")

    result = iris.run_investigation(question)

    print("\n=== IRIS SPL SUMMARY ===")
    print(result["summary"])
    print("\n=== KEY ENTITIES ===")
    for k, v in result["entities"].items():
        print(f"- {k}: {', '.join(v) if v else 'None'}")

    print("\n=== SUGGESTED ACTIONS ===")
    for action in result["actions"]:
        print(f"- {action}")

if __name__ == "__main__":
    main()
