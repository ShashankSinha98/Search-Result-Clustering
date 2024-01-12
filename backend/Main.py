from KMeans import queryCluster

if __name__ =="__main__":
    while int(input("Continue (1/0)?: ")) != 0:
        # Ask for inputs from user
        query = input("Enter Query: ")
        no_of_results = int(input("No of results expected: "))
        K = int(input("No of clusters: "))
        json_res = queryCluster(query, no_of_results, K,  True)
        print(json_res)