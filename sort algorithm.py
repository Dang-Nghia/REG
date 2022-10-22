import time
#bubble sort
#bubbel sort (sắp xếp nổi bọt) duyệt qua các danh sách và so sánh các cặp phần tử liền kề.
#và hoán đổi nếu chúng không đúng thứ tự và lặp lại cho đến khi danh sách đc sắp xếp.
#vì lặp đi lặp lại các phần tử chưa được sắp xếp nên bubble sort có độ phức tạp trong trường hợp
#xấu nhất là O(n**2)
def bubble_sort(lst):
    def swap(a,b):#thực hiện đối chỗ 2 phần tử trong danh sách có index a và index b
        lst[a] , lst[b] = lst[b],lst[a]
    swaped = True # đối tượng kết thúc vòng lặp
    x = -1 #khởi tạo biến của vòng lặp
    while swaped:
        swaped = False
        x += 1# gia tăng giá tri cho biến của vòng lặp
        for i in range(1,len(lst) - x):#lặp lại so sánh giữa phần tử thứ i và thứ i - 1 của danh sách
            #mỗi khi hoàn thành một vòng lặp for, có một phần tử của danh sách đã được đưa về đúng vị trí
            #vị trí ở ngay sau phần tử trước đó của vòng lặp, nếu là phần tử đầu tiên nó là phần tử lớn nhất
            #và đứng ở cuối của danh sách.
            #len(lst) - x thể hiện chó số phần tử của danh sách đã chưa được sắp xếp
            if lst[i-1] > lst[i]:
                swap(i-1,i)
                swaped = True
    return lst
#selection sort: sắp xếp chọn
#chia danh sách thành 2 phần danh sách con các mục đã được sắp xếp và danh sách con các mục chưa được sắp xếp
#tìm phần tử nhỏ nhất của danh sách con chưa được sắp xếp và đặt vàp cuối của danh sách con đã được sắp xếp
#thực hiên liên tục cho tới khi danh sách con chưa được sắp xếp rỗng
def selection_sort(lst):
    for i in range(len(lst)):
        # i là index của phần tử nhỏ nhất của danh sách chưa được sắp xếp
        for j in range(i+1,len(lst)):#so sánh lst[i] với các phần tử khác trong danh sách chưa được sắp xếp
            if lst[i] > lst[j]:
                lst[i],lst[j] = lst[j],lst[i]
        #khi vòng lặp kết thúc phần tử nhỏ nhất của danh sách chưa được sắp xếp đã đứng cuối của danh sách
        #đã được sắp xếp
    return lst
#insertion sort(sắp xếp chèn)
#insertion sort được cho là nhanh và đơn giản hơn bubble sort và selection sort.
#trên mỗi lần lặp insertion sort sẽ loại bỏ một phần tử ra khỏi mảng. Sau đó nó tìm vị trí mà phần tử này
#thuộc về trong một mảng được sắp xếp khác. Lặp lại như vậy cho đến khi không còn yếu tố đầu vào nào

def insertion_sort(lst):
    for i in range(len(lst)):
        cursor = lst[i] # chọn một phần tử trong danh sách
        pos = i#lấy index của phần tử dược chọn
        while pos > 0 and lst[pos - 1] > cursor:
            #lặp liên tục để tìm vị trí mà phần tử thuôc về trong mảng
            lst[pos] = lst[pos - 1]
            pos -=1
        lst[pos] = cursor
    return lst

#merge sort (sắp xếp trộn)
#merge sort dựa trên thuật toán chia để trị
#liên tục chia nhỏ mảng ban đầu thành các mảng nhỏ hơn đến khi không thể chia nữa
#sau đó sắp xếp và hợp chúng lại với nhau
def merge_sort(lst):
    #xác định điều kiện kết thúc đệ quy
    if len(lst) > 1:
        #lấy index ở giữa để chia list
        mid = len(lst) // 2
        #chia list thành 2 phần
        lst_left = lst[: mid]
        lst_right = lst[mid :]
        #đệ quy
        merge_sort(lst_left)
        merge_sort(lst_right)
        #khởi tạo giá trị lặp cho list đc chia nhỏ
        iter_l = 0
        iter_r = 0
        #index list chứa các giá trị sau khi xắp xếp
        k = 0
        #vòng lặp
        while iter_l < len(lst_left) and iter_r < len(lst_right):
            #so sánh các phần tử trong 2 list với nhau
            #và đặt chúng lại vào list ban đầu
            if lst_left[iter_l] < lst_right[iter_r]:
                lst[k] = lst_left[iter_l]
                iter_l += 1
                k += 1
            else:
                lst[k] = lst_right[iter_r]
                iter_r += 1
                k += 1
        #đặt các phần tử còn lại của các list vào list ban đầu
        while iter_l < len(lst_left):
            lst[k] = lst_left[iter_l]
            iter_l += 1
            k += 1
        while iter_r < len(lst_right):
            lst[k] = lst_right[iter_r]
            iter_r += 1
            k += 1
    return lst
mylist = [i for i in range(10000,1,-2)]
##merge sort
lst = mylist.copy()
start = time.time()
merge_sort(lst)
print(lst)
end = time.time()
run_time = end - start
print("merge sort take {}".format(run_time))
##### buble sort
lst = mylist.copy()
start = time.time()
bubble_sort(lst)
print(lst)
end = time.time()
run_time = end - start
print("buble sort take {}".format(run_time))
####selection sort
lst = mylist.copy()
start = time.time()
selection_sort(lst)
print(lst)
end = time.time()
run_time = end - start
print("selection sort take {}".format(run_time))
####insertion sort
lst = mylist.copy()
start = time.time()
insertion_sort(lst)
print(lst)
end = time.time()
run_time = end - start
print("insertion sort take {}".format(run_time))



