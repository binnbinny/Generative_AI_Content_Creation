from src.text_generator import TextGenerator


def test_story_generation():
    generator = TextGenerator()

    prompt = "Write a short story about a student discovering a secret room in college."

    result = generator.generate(prompt)

    assert result is not None
    assert len(result.strip()) > 0


def test_education_generation():
    generator = TextGenerator()

    prompt = "Explain photosynthesis in simple language for a school student."

    result = generator.generate(prompt)

    assert result is not None
    assert len(result.strip()) > 0


def test_marketing_generation():
    generator = TextGenerator()

    prompt = (
        "Create a short advertisement for a smartwatch with fitness tracking, "
        "heart-rate monitoring, and a long-lasting battery."
    )

    result = generator.generate(prompt)

    assert result is not None
    assert len(result.strip()) > 0


def test_empty_prompt():
    generator = TextGenerator()

    prompt = ""

    result = generator.generate(prompt)

    assert result is not None