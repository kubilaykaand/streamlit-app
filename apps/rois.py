"""
Define ROIs for the application.
"""

import geemap.foliumap as geemap
import ee

geemap.ee_initialize()

fire_cases = {
    "Creek Fire, CA 2020": {
        "region": ee.Geometry.Polygon(
            [
                [-121.003418, 36.848857],
                [-121.003418, 39.049052],
                [-117.905273, 39.049052],
                [-117.905273, 36.848857],
                [-121.003418, 36.848857],
            ]
        ),
        "date_range": ["2020-09-05", "2020-09-06"],
    },
    "Marmaris 2021": {
        "region": ee.Geometry.Polygon(
            [
                [28.126911034358155, 36.80216004174086],
                [28.133434259593162, 36.79473723496511],
                [28.13034431097759, 36.79226280609539],
                [28.128971000557843, 36.788688490022324],
                [28.12622437968218, 36.78318921661521],
                [28.125881052181388, 36.77906450261417],
                [28.125881052284647, 36.775764571598756],
                [28.129314328643268, 36.77328953017901],
                [28.13515089848889, 36.76696406124185],
                [28.142360778699654, 36.765038815028426],
                [28.150257314174414, 36.76173828040925],
                [28.154033918148645, 36.75651214332313],
                [28.145794055197182, 36.75403648030693],
                [28.130000984428722, 36.75513678454526],
                [28.12416441499122, 36.749360009794984],
                [28.122104449467297, 36.742757449029895],
                [28.12004448394798, 36.736429461934364],
                [28.123134432775956, 36.72927545718687],
                [28.138927503506032, 36.72129520421004],
                [28.1416741246225, 36.71413978946934],
                [28.15678053985734, 36.71028659795444],
                [28.1784101797367, 36.70753420000191],
                [28.188023353003597, 36.71469022998447],
                [28.202099785297232, 36.71056183244624],
                [28.21308626913968, 36.71771758038481],
                [28.236775874864467, 36.72019441450111],
                [28.25823555226075, 36.73023383337424],
                [28.27480814218691, 36.736078731390855],
                [28.282754820265666, 36.732672995642496],
                [28.28260963285075, 36.72188839052514],
                [28.291291956260768, 36.71952080428943],
                [28.304046235176582, 36.731269601171164],
                [28.29325956822912, 36.74897613438644],
                [28.288893936056002, 36.75095384064875],
                [28.280187391124286, 36.745891114728046],
                [28.27205617438109, 36.7513368886062],
                [28.272796192900962, 36.75956198371465],
                [28.26046381595701, 36.77027587024111],
                [28.254125697318123, 36.77137129288446],
                [28.25018339685549, 36.773225847532586],
                [28.257824453051438, 36.79044541636305],
                [28.24899380990818, 36.80064966243652],
                [28.243400832808614, 36.80238276023182],
                [28.234680643442395, 36.804347460425845],
                [28.24593660563526, 36.816254311952854],
                [28.246238458918377, 36.827156307916475],
                [28.252737003258257, 36.84167415160878],
                [28.247740865426227, 36.848520542179216],
                [28.235799421878603, 36.85455148750602],
                [28.23188801122296, 36.85440434420191],
                [28.226156310160874, 36.84883553901553],
                [28.210589923727333, 36.84728692178874],
                [28.210190245200913, 36.842251537871654],
                [28.203125174722587, 36.83629948753591],
                [28.188436438125066, 36.83071217376159],
                [28.138394563293843, 36.81522305715212],
            ]
        ),
        "date_range": ["2021-07-30", "2021-08-10"],
    },
}
