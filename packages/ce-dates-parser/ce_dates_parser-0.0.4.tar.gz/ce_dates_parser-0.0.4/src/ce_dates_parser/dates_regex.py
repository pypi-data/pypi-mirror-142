import re

year = r'((19[0-9]{2})|(2[0-9]{3}))'
range_link = r'\s*(-{1}|(do){1}|(to){1}|–{1})\s*'
conjunction = r'\s*[–/| .-]\s*'
present = r'(now)|(current)|(present)|(currently)|(teraz)|(obecnie)|(dzisiaj)'
day_of_month = r'([0-9]|([0-2][0-9])|(3[0-1]))'
month = r'((0?[1-9])|([0-1][0-2]))'
roman_month = r'((v?i{1,3})|(i?(x|v))|(xi{1,2}))'
polish_months = r'((st((yczeń)|(yczen)|(ycze)|(ycz)|(yc)|(y))?)|(lut(y)?)|(mar((zec)|(ze)|(z))?)|(kw((iecien)|(iecień)|(iecie)|(ieci)|(iec)|(ie)|(i))?)|(maj)|(cz((erwiec)|(erwie)|(erwi)|(erw)|(er)|(e))?)|(lip((iec)|(ie)|(i))?)|(sier((pień)|(pien)|(pie)|(pi)|(p))?)|(wrz((esień)|(esien)|(esie)|(esi)|(es)|(e))?)|(pa((ź)|(z))((dziernik)|(dzierni)|(dziern)|(dzier)|(dzie)|(dzi)|(dz)|(d))?)|(lis((topad)|(topa)|(top)|(to)|(t))?)|(gr((udzień)|(udzien)|(udzie)|(udzi)|(udz)|(ud)|(u))?))'
english_months = r'((jan((uary)|(uar)|(ua)|(u))?)|(feb((ruary)|(ruar)|(rua)|(ru)|(r))?)|(mar((ch)|(c))?)|(apr((il)|(i))?)|(may)|(jun(e)?)|(jul(y?))|(aug((ust)|(us)|(u))?)|(sep((tember)|(tembe)|(temb)|(tem)|(te)|(t))?)|(oct((ober)|(obe)|(ob)|(o))?)|(nov((ember)|(embe)|(emb)|(em)|(e))?)|(dec((ember)|(embe)|(emb)|(em)|(e))?))'
month_with_year = month + conjunction + year
european_date = day_of_month + conjunction + month_with_year
american_date = month + conjunction + day_of_month + conjunction + year
roman_date = roman_month + conjunction + year

# ex. 2021 - july 2022
year_month_year_regex = r'\s' + year + r'(' + range_link + english_months + r'?\s*' + year + r')?\s'
# ex. 31.12.2021 - 31.11.2022
european_date_range_regex = r'\s' + european_date + r'(' + range_link + r'(' + european_date + r'|' + present + r'))?\s'
# ex. 12.31.2021 - 11.30.2022
american_date_range_regex = r'\s' + american_date + r'(' + range_link + r'((' + american_date + r')|' + present + r'))?\s'
# ex. 14 july 2021 to 15 june 2022
english_months_range_regex = r'\s' + day_of_month + r'?\s*' + english_months + r'\s+' + year + r'?' + r'(' + range_link + day_of_month + r'?\s*((' + english_months + r'\s*' + year + r'?)|' + present + r'))?\s'
# ex. 14 lipiec 2021 to 15 czerwiec 2022
polish_months_range_regex = r'\s' + day_of_month + r'?\s*' + polish_months + r'\s+' + year + r'?' + r'(' + range_link + day_of_month + r'?\s*((' + polish_months + r'\s+' + year + r'?)|' + present + r'))?\s'
# ex. 12.2021 - 11.2022
month_with_year_range_regex = r'\s' + month_with_year + r'((' + range_link + r'((' + month_with_year + r')|' + present + r'))|(\s))\s'
# ex. 2022 - 2023
years_only_range_regex = r'\s' + year + r'\s*(' + range_link + r'(' + year + r'|' + present + r'))?\s'
# ex. II 2021 to III 2023
roman_date_range_regex = r'\s' + roman_date + r'(' + range_link + r'' + roman_date + r')?\s'
# ex. 2021.03 - 2022.05
year_first_range_regex = r'\s' + year + conjunction + month + '(' + conjunction + day_of_month + r')?' + r'(' + range_link + r'' + year + conjunction + month + '(' + conjunction + day_of_month + r')?)?\s'

list_of_regex = [
    year_month_year_regex,
    european_date_range_regex,
    american_date_range_regex,
    english_months_range_regex,
    polish_months_range_regex,
    month_with_year_range_regex,
    years_only_range_regex,
    roman_date_range_regex,
    year_first_range_regex
]

generic_re = re.compile('|'.join(list_of_regex))
