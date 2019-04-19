from collections import namedtuple

Regression = namedtuple("Regression", ["wave", "hscale", "period", "phase", "expected"])
Regression.__new__.__defaults__ = ("", 1, 1, 0, [])


basic = [
    Regression(wave="P", expected=['Pclk', 'nclk']),
    Regression(wave="P", hscale=2, expected=['Pclk', '111', 'nclk', '000']),
    Regression(wave="P", period=2, expected=['Pclk', '111', 'nclk', '000']),
    Regression(wave="P", hscale=2, period=0.5, expected=['Pclk', 'nclk']),
    Regression(wave="P", phase=1, expected=['nclk']),
    Regression(wave="P", hscale=2, phase=2, expected=['nclk', '000']),
    Regression(wave="P.", expected=['Pclk', 'nclk', 'Pclk', 'nclk']),
    Regression(wave="P..", expected=['Pclk', 'nclk', 'Pclk', 'nclk', 'Pclk', 'nclk']),
    Regression(wave="P.", hscale=2, expected=['Pclk', '111', 'nclk', '000', 'Pclk', '111', 'nclk', '000']),
    Regression(wave="P..", hscale=2, expected=['Pclk', '111', 'nclk', '000', 'Pclk', '111', 'nclk', '000',
                                               'Pclk', '111', 'nclk', '000']),
    Regression(wave="0", expected=['000', '000']),
    Regression(wave="1", expected=['111', '111']),
    Regression(wave="01", expected=['000', '000', '0m1', '111']),
    Regression(wave="01", hscale=2, expected=['000', '000', '000', '000', '0m1', '111', '111', '111']),
    Regression(wave="01.0", expected=['000', '000', '0m1', '111', '111', '111', '1m0', '000']),
    Regression(wave="01.zx=ud.23.45",
               expected=['000', '000', '0m1', '111', '111', '111', '1mz', 'zzz', 'zmx', 'xxx', 'xmv-2', 'vvv-2',
                         'vmu-2', 'uuu', 'umd', 'ddd', 'ddd', 'ddd', 'dmv-2', 'vvv-2', 'vmv-2-3', 'vvv-3', 'vvv-3',
                         'vvv-3', 'vmv-3-4', 'vvv-4', 'vmv-4-5', 'vvv-5']),
    Regression(wave="01.zx=ud.23.45", hscale=2,
               expected=['000', '000', '000', '000', '0m1', '111', '111', '111', '111', '111', '111', '111', '1mz',
                         'zzz', 'zzz', 'zzz', 'zmx', 'xxx', 'xxx', 'xxx', 'xmv-2', 'vvv-2', 'vvv-2', 'vvv-2', 'vmu-2',
                         'uuu', 'uuu', 'uuu', 'umd', 'ddd', 'ddd', 'ddd', 'ddd', 'ddd', 'ddd', 'ddd', 'dmv-2', 'vvv-2',
                         'vvv-2', 'vvv-2', 'vmv-2-3', 'vvv-3', 'vvv-3', 'vvv-3', 'vvv-3', 'vvv-3', 'vvv-3',
                         'vvv-3', 'vmv-3-4', 'vvv-4', 'vvv-4', 'vvv-4', 'vmv-4-5', 'vvv-5', 'vvv-5', 'vvv-5']),
    Regression(wave="phnlPHNL", expected=['pclk', 'nclk', 'pclk', '111', 'nclk', 'pclk', 'nclk', '000', 'Pclk', 'nclk',
                                          'Pclk', '111', 'Nclk', 'pclk', 'Nclk', '000']),
    Regression(wave="xhlhLHl.", expected=['xxx', 'xxx', 'pclk', '111', 'nclk', '000', 'pclk', '111', 'Nclk', '000',
                                          'Pclk', '111', 'nclk', '000', '000', '000']),
    Regression(wave="hpHplnLn", expected=['111', '111', '111', 'nclk', 'Pclk', '111', '111', 'nclk', '000', '000',
                                          '000', 'pclk', 'Nclk', '000', '000', 'pclk']),
    Regression(wave="nhNhplPl", expected=['nclk', 'pclk', '111', '111', 'Nclk', 'pclk', '111', '111', '111', 'nclk',
                                          '000', '000', 'Pclk', 'nclk', '000', '000']),
    Regression(wave="xlh.L.Hx", expected=['xxx', 'xxx', 'nclk', '000', 'pclk', '111', '111', '111', 'Nclk', '000',
                                          '000', '000', 'Pclk', '111', '1mx', 'xxx'])
]
subcycle = [
    Regression(wave="0<10>1", expected=['000', '000', '0m1', '1m0', '0m1', '111']),
    Regression(wave="<10>10", expected=['111', '1m0', '0m1', '111', '1m0', '000']),
    Regression(wave="<x0>1x", expected=['xxx', 'xm0', '0m1', '111', '1mx', 'xxx']),
    Regression(wave="<01>", expected=['000', '0m1']),
    Regression(wave="x.<01...0>x", expected=['xxx', 'xxx', 'xxx', 'xxx', 'xm0', '0m1', '111', '111', '111', '1m0',
                                             '0mx', 'xxx'])
]

all = basic + subcycle