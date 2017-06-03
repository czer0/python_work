def make_shirt(shirt_size, shirt_text):
    """Display shirt size and printed text."""
    print("\nShirt order is " + shirt_size.title() + ".")
    print("Text on shirt should read " + shirt_text.title() + ".")

make_shirt('large', 'i like ducks')
make_shirt(shirt_size = 'small', shirt_text = 'i mine at a loss')
