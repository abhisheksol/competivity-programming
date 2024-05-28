def cal(num_of_stu,costs):
    total_cost=sum(costs)
    avg=total_cost/num_of_stu
    exchange_amt=0
    for cost in costs:
        if cost<avg:
            exchange_amt+=round(avg-cost)
    return exchange_amt



def main():
    while True:
        num_of_stu=int(input("enter the No od stu:"))
        if num_of_stu==0:
            break
        costs=[float(input(f"enter the amt of stu {i+1} :")) for i in range(num_of_stu)]
        print(cal(num_of_stu,costs))

main()