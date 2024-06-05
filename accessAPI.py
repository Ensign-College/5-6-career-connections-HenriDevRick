import requests
import json

base_url = 'https://openscriptureapi.org/api/scriptures/v1/lds/en/volume/bookofmormon/'

def get_chapter_summary(book, chapter):
    url = f'{base_url}{book}/{chapter}'
    response = requests.get(url)
    data = response.json()
    
    # Extract the summary from the JSON data
    summary = data['chapter']['summary'] if 'summary' in data['chapter'] else "No summary available for this chapter."
    return summary

def main():
    print("Welcome to the Book of Mormon Summary Tool!")
    while True:
        book = input("Which book of the Book of Mormon would you like? ")
        chapter = input(f"Which chapter of {book} are you interested in? ")
        
        # Retrieve and print the summary for the specified book and chapter
        summary = get_chapter_summary(book, chapter)
        print(f"Summary of {book} chapter {chapter}:")
        print(summary)
        
        # Ask the user if they would like to view another summary
        another = input("Would you like to view another (Y/N)? ").strip().upper()
        if another != 'Y':
            break

    print("Thank you for using Book of Mormon Summary Tool!")

if __name__ == "__main__":
    main()

