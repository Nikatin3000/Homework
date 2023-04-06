def stop_words(words: list):
    def decorator(func):
        def repl(*args):
            resultat = func(*args)
            for word in words:
                resultat = resultat.replace(word, '*')
            return resultat
        return repl
    return decorator


@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


assert create_slogan("Steve") == "Steve drinks * in his brand new *!"

print(create_slogan('Vadim'))