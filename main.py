from serpapi import GoogleSearch

params = {
  "api_key": "8e952a1324a7b295488f7ed8c8b5a414f3b1109b1f97ffe59fc3555eb28112f7",
  "engine": "google_scholar",
  "q": "Coffee",
  "hl": "en"
}

search = GoogleSearch(params)
results = search.get_dict()
results_1 = results['organic_results']

print(results)
print("Ваш запрос : " + results['search_parameters']['q'])
print("Всего результатов: " + str(results['search_information']['total_results']))
print("Больше результатов: " + results['search_metadata']['google_scholar_url'])
print("НАЗВАНИЕ: " + str(results_1[1]))
print("НАЗВАНИЕ: " + str(results_1[1]['title']) +
      "\nОписание" + str(results_1[1]['snippet']) +
      "\nССЫЛКА: " + str(results_1[1]['link']) +
      "\nPDF: " + str(results_1[1]['resources'][0]['link']))
print("НАЗВАНИЕ: " + str(results_1[2]))
