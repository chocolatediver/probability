from ml.registry import ModelRegistry

def main():
    print("Available model registry")
    print("=" * 40)
    for spec in ModelRegistry().list_models():
        status = "available" if spec.available else "missing optional dependency"
        print(f"{spec.name:20s} | {spec.model_type:10s} | {status} | {spec.description}")

if __name__ == "__main__":
    main()
