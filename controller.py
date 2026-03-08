

#controller
def main():
    print("Collecting....")
    items=[]

    items+=collect_arxiv()
    items+=collect_anthropic()
    items+=collect_deepmind()
    items+=collect_news()
    print(f"Collected{len(items)}...")
    shortlist= relevance_filter(items)
    if len(shortlist)==0:
      print ("Nothing interesting this week")
      return
    print(f"Shortlisted{len(shortlist)}")
    decision_spec = run_decision(shortlist, mode="infer") # Changed `items` to `shortlist`
    print(decision_spec)
    if decision_spec:
        write = writer(decision_spec)
        print(write)
    else:
        print("No valid decision specification generated.")




if __name__ =="__main__":
    main()