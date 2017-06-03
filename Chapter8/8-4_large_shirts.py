def make_shirt(shirt_size = 'large', shirt_text = 'i love python'):
    """Display shirt size and printed text."""
    print("\nShirt order is " + shirt_size.title() + ".")
    print("Text on shirt should read " + shirt_text.title() + ".")

make_shirt()
make_shirt('medium', 'Who wants fries?')
make_shirt('large', 'i like ducks')
make_shirt(shirt_size = 'small', shirt_text = 'i mine at a loss')

