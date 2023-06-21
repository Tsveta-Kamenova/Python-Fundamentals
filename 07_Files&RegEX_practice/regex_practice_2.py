import re
dict = {"&":"__amp","#":"__hsh","1":"5","5":"6"}

var_str = "a1asda&fj#ahdk5adfls"
var_regex = new_Regex(String.Join("|",map.Keys))
var_newStr = regex.Replace(str, m => map[m.Value])