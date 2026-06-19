from models.text_generator import TextGenerator

def test_generate():
    gen = TextGenerator()
    result = gen.generate_text("Hello", 20)
    assert isinstance(result, str)
    print(result)

test_generate()