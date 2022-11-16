# Deep Classifier Project

## Workflow

1. Update configuration: config.yaml file.
2. Update secrets.yaml (contains any secret keys)[optional]
3. update params.yaml
4. update entity in src/deepClassifier/entity
5. update configuration manager(config folder) in src/deepClassifier/config
6. Update components in src/deepClassifier/components
7. update pipeline in src/deepClassifier/pipeline
8. Test run pipeline stage
9. Run tox for testing package
10. update dvc.yaml
11. run "dvc repro" command(reproduce) for running all stages in pipeline

![img](https://raw.githubusercontent.com/Vikaslakkacs/Deep_classifier/4a93274b8f2140c657e37646c6ec747c9d975451/docs/images/Data%20Ingestion%402x%20(1).png)