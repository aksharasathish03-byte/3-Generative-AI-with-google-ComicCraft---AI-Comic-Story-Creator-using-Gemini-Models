def generate_comic_story(idea):
    story = f"""
Comic Story Title: {idea}

Panel 1:
The story begins with the idea: {idea}.

Panel 2:
The characters start their adventure and face an interesting situation.

Panel 3:
They find a creative solution to the problem.

Panel 4:
The story ends with a happy and meaningful conclusion.
"""
    return story


print("Welcome to ComicCraft - AI Comic Story Creator")

idea = input("Enter your comic story idea: ")

result = generate_comic_story(idea)

print("\nGenerated Comic Story:")
print(result)
