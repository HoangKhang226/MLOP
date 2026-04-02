import os
from pathlib import Path

def test_project_structure():
    """
    Kiểm tra xem các folder quan trọng có tồn tại không
    """
    assert os.path.exists("src/mlProject")
    assert os.path.exists("config/config.yaml")
    assert os.path.exists("requirements.txt")

def test_pipeline_modules():
    """
    Kiểm tra xem có thể import các giai đoạn chính của pipeline không
    """
    try:
        # Sửa lại thành from src.mlProject... cho khớp với project
        from src.mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
        from src.mlProject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
        assert True
    except ImportError as e:
        assert False, f"Không thể import pipeline modules: {e}"
