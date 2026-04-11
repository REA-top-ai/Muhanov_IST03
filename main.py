from API_app.API_methods import get_everything, summarize_with_mistral

topic = "Ruble"   #тема
if __name__ =='__main__':
    result = get_everything('everything','1b48faa621944374aa3aa1eb5966422d',{'q':topic})
    articles = result.get("articles", [])

    text = summarize_with_mistral('7DO6DoAmULzNb6AtWdnjkY2eR2FH5sKn', articles)

    with open("../../text.txt", "w", encoding="utf-8") as f:
        f.write(text)
    with open("../../text.txt", "r", encoding="utf-8") as f:
        content = f.read()
    print(content)



