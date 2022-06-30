# convert jan-> january or mar -> march

monthConverstion = {
    "Jan" : "January",
    "Feb" : "February",
    "Mar" : "March",
    "Apr" : "April",
    "May" :  "May", 
    "Jun" : "June", 
    "Jul" : "July", 
    "Aug" : "August", 
    "Sep" : "September", 
    "Oct" : "October", 
    "Nov" : "November",
    "Dec" : "December"
}

print(monthConverstion.get("dec","Not a valid key"))
print(monthConverstion.get("Dec","Not a valid key"))