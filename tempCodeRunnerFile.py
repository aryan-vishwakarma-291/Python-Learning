pen('student.txt' , 'r') as  f:
      for line in f:
            name, marks , city = line.strip().split(',')
            print(f'{name:<15} | {marks:>5} | {city}')
            print("----------")
