from dataclasses import dataclass


@dataclass
class DataTest:

    def get_data_input(self) -> dict:
        return {
            'Município': self.citys,
            'UF': self.uf,
            'Mês': self.months,
            '2007': self.d_2007,
            '2008': self.d_2008,
            '2009': self.d_2009,
            '2010': self.d_2010,
            '2011': self.d_2011,
            '2012': self.d_2012,
            '2013': self.d_2013,
            '2014': self.d_2014,
            '2015': self.d_2015,
            '2016': self.d_2016,
            '2017': self.d_2017,
            '2018': self.d_2018,
            '2019': self.d_2019,
        }

    def get_data_output_correct_yearly(self, info=()):
        output_correct, period_index, period = info
        years = [f'{y}' for y in range(2007, 2020)]

        result_list = []

        for index, value in enumerate(output_correct):
            tuple_value = (period_index, period, years[index], '', value)
            result_list.append(tuple_value)

        return result_list

    citys = ['Acrelândia'] * 12
    uf = ['AC'] * 12
    months = [month for month in range(1, 13)]

    d_2007 = [271775.97, 280869.8, 267766.24,
              380866.48, 321605.33, 335560.57,
              284149.29, 292019.94, 300696.13,
              291828.37, 331692.59, 414820.39]

    d_2008 = [450935.06, 458391.25, 373189.77,
              443127.06, 448585.1, 400116.39,
              367068.88, 429645.13, 391993.61,
              376058.77, 461230.05, 489041.58]

    d_2009 = [484772.76, 458508.64, 402307.75,
              398573.19, 485830.6, 441084.51,
              360411.62, 408999.51, 380006.35,
              421930.92, 499635.98, 520305.36, ]

    d_2010 = [407833.04, 471105.76, 399129.32,
              453902.42, 549101.9, 489726.37,
              392017.64, 495703.49, 430470.25,
              447468.92, 528157, 617770.96]

    d_2011 = [597904.87, 639142, 476030.76,
              565926.97, 626097.21, 567832.51,
              511015.56, 530522.55, 440620.85,
              537753.76, 559874.19, 634920.6]

    d_2012 = [527997.88, 609636.53, 478494.75,
              601585.35, 639171.8, 570955.09,
              475867.38, 499718.14, 450156.38,
              471403.84, 581780.66, 628729.31]

    d_2013 = [583661.6, 736534.13, 498639.44,
              549812.76, 663995.2, 586470.6,
              456447.61, 546395.78, 483283.26,
              479235.84, 654128.07, 641397.81]

    d_2014 = [720360.73, 780017.31, 509898.4,
              569296.5, 742261.04, 588409.09,
              531154.33, 599519.56, 561581.83,
              527705.19, 646300.33, 705448.22]

    d_2015 = [742658.21, 766779.71, 616306.35,
              601038, 705553.43, 649058.35,
              511760.42, 588948.87, 522617.91,
              550245.62, 633989.09, 713670.03]

    d_2016 = [679012.21, 755635.27, 549970.96,
              609178.96, 747842.28, 633050.45,
              522797.78, 599089.05, 510491.33,
              591094.01, 1002102.02, 1185681.23]

    d_2017 = [748780.61, 850714.86, 617978.2,
              685174.68, 772153.06, 756646.18,
              603845.65, 663319.33, 605563.7,
              672344.49, 658986.27, 850200.07]

    d_2018 = [740381.02, 880849.33, 642454.98,
              661647.05, 783355.47, 734097.56,
              576469.32, 668887.33, 561228.16,
              624771.58, 727412.46, 1066328.05]

    d_2019 = [861747.15, 900609.50, 711703.16,
              718405.94, 825357.96, 676517.09,
              760446.15, 696022.61, 667612.52,
              651903.12, 757361.32,  0.00]
