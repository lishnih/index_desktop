#!/usr/bin/env python
# coding=utf-8
# Stan 2012-03-10

import re
import xlrd

from reg import reg_object
from models import Sheet
from lib.sheet_parse import parse_doc, parse_table


def proceed_sheet(sh, options, FILE, i=None):
    sheet_dict = dict(
        _file = FILE,
        sh = sh,
        seq = i,
    )
    SHEET = reg_object(Sheet, sheet_dict, PARENT=FILE)

    sheet_test = options.get('sheet_test')
    if sheet_test:
        row, col, test_pattern = sheet_test
        test_cell = get_str(sh, row, col)
        res = re.search(test_pattern, test_cell)
        if res:
            SHEET.sheet_test = test_cell

    if 'doc' in options:
        doc_options = options.get('doc')
        parse_doc(sh, doc_options, SHEET)

    if 'table' in options:
        table_options = options.get('table')
        parse_table(sh, table_options, SHEET)
