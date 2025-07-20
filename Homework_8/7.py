"""
Написать функцию (без регулярных выражений), которая принимает текстовую строку 
и возвращает словарь, который содержит информацию о количестве 
символов, слов, строк и предложений в тексте. 
Затем создайте вторую функцию, которая принимает этот словарь, 
и выводит его содержимое в удобном и красивом формате. 

"""

# Анализ текста
def analyze_text(text):
    try:
        char_count = len(text)
        word_count = len(text.split())
        line_count = len(text.split('\n'))
        sentence_count = sum(text.count(end) for end in ('.', '!', '?'))
        
        return {
            "Characters": char_count,
            "Words": word_count,
            "Lines": line_count,
            "Sentences": sentence_count
        }
    except Exception as e:
        return {"error": str(e)}
    
    
# Вывод результата  
def print_analysis(result):
    if "error" in result:
        print("Error:", result["error"])
    else:
        print("Text Analysis Result:")
        print("----------------------")
        for key, value in result.items():
            print(f"{key:<12}: {value}")


sample_text = """Hello world! This is a test.
It has multiple lines. And some questions?!
"""

stats = analyze_text(sample_text)
print_analysis(stats)

