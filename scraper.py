import scraperwiki
import lxml.html
from SA1s import SA1s

# a=[101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,230,231,232,233,234,235,236,237,301,302,303,304,305,306,307,308,309,310,311,312,313,314,315,316,317,318,319,320,321,322,323,324,325,326,327,328,329,330,401,402,403,404,405,406,407,408,409,410,411,501,502,503,504,505,506,507,508,509,510,511,512,513,514,515,601,602,603,604,605,701,702,801,802]
a=SA1s
b=[]
for i in a:
    b.append("http://www.censusdata.abs.gov.au/census_services/getproduct/census/2011/quickstat/"+str(i)) 
for s in range(scraperwiki.sqlite.get_var('upto'), len(b)):
    html = scraperwiki.scrape(b[s])
    root = lxml.html.fromstring(html)
    sa1 = root.cssselect(".geo")[0]
    sa1code = (root.cssselect(".geoCode")[0].text).split(' ')
    # sa1code = sa1code[1].split('(')
    sa1code = int(sa1code[1])
    scraperwiki.sqlite.save_var('upto', a.index(sa1code))

    sourceurl = b[s]
    tables = []
    tablelength = len(root.cssselect("td"))
    for x in range(0, tablelength):
        tables.append(root.cssselect("td")[x].text)
    # htmldump = lxml.etree.tostring(root)
    # twoormorelang = htmldump.split('"Households where two or more languages are spoken", areaPercent: QuickStats.formatValue(')[1].split(')')[0]
    # unemployed = tables[(tables.index('Unemployed') + 2)]
    # workedfulltime = tables[(tables.index('Worked full-time') + 2)]
    # workedparttime = tables[(tables.index('Worked part-time') + 2)]
    # awayfromwork = tables[(tables.index('Away from work') + 2)]
    # tertiary = tables[(tables.index('University or tertiary institution') + 2)]
    rent_under_30pc = tables[(tables.index('Households where rent payments are less than 30% of household income') + 2)]
    rent_over_30pc = tables[(tables.index('Households where rent payments are 30%, or greater, of household income') + 2)]
    mortgage_under_30pc = tables[(tables.index('Households where mortgage payments are less than 30% of household income') + 2)]
    mortgage_over_30pc = tables[(tables.index('Households where mortgage payments are 30%, or greater, of household income') + 2)]

    
    print sa1.text
    print b[s]

    data = {}
    data['sa1'] = sa1.text
    data['sa1code'] = sa1code
    data['rent_under_30pc'] = rent_under_30pc
    data['rent_over_30pc'] = rent_over_30pc
    data['mortgage_under_30pc'] = mortgage_under_30pc
    data['mortgage_over_30pc'] = mortgage_over_30pc
    data['source'] = b[s]
    scraperwiki.sqlite.save(unique_keys=["sa1"], data=data)