a = {
    "fw_list": [1701,
                2222,
                33333],
    "b_fw1": 11111,
    "b_fw2": 22222,
    "part_num": 111111
}

fw_from_pcba = 1701
if fw_from_pcba in a["fw_list"]:
    print('FW %s' % fw_from_pcba)
    print("PASS")
else:
    print("FAIL")
