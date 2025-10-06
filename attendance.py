total_classes = int(input("Enter the total number of classes held: "))
attended_classes = int(input("Enter the number of classes attended: "))
atnd_pcent = (attended_classes / total_classes) * 100
if total_classes > 0 and attended_classes > 0:
    
    print("Classes Held:", total_classes)
    print("Classes Attended:", attended_classes)
    print("Attendance:",  atnd_pcent,"%")
else:
    print("Total classes or attended classes cannot be zero.")
