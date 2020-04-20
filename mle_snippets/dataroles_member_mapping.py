import pandas as pd


def create_data_role_json_file():
    pass


def complex_df_agg_type1():
    """This function aggregates dataframe column values into List"""
    data = [{'group_id': 'a_group', 'position_nbr': '12345'},
            {'group_id': 'a_group', 'position_nbr': '34567'},
            {'group_id': 'b_group', 'position_nbr': '464566'},
            {'group_id': 'c_group'}]

    # Creates DataFrame.
    df = pd.DataFrame(data)
    print(df)
    print(df.groupby('group_id')['position_nbr'].apply(list))

    by_group_id = df.groupby('group_id')

    by_group_id.

   # by_group_id.apply()

   # print(type(by_group_id))
    print('>>>>>>>>>>>>> start')
    print(by_group_id)
    print(by_group_id['position_nbr'])
    print(by_group_id['position_nbr'].apply(list))
    con = by_group_id['position_nbr'].apply(list)
    print(con)
    print(type(con))
    print(by_group_id['position_nbr'])
    print('>>>>>>>>>>>>> End')


    data_roles = []
    for g, gl in by_group_id:


        tag_list = [g]

        pst_nbr_list = gl['position_nbr'].values.tolist()

        pst_list = [x for x in pst_nbr_list if x.lower() != 'nan']

        if len(pst_list) != 0:
            tag_list.append(pst_list)

        msg_list = [f'msg:{n}' for n in tag_list]
        msg_list.append('ki:wfs_models')
        alert_list = [f'alert:{n}:wfs_models' for n in tag_list]
        msg_list.append(alert_list)

        group = {'name': g, 'permissions': msg_list}
        data_roles.append(group)


    ps_list = ['1', '2', '3']
    trns_ps_list = []
    for n in ps_list:
        msg_str = f"msg:{n}"
        trns_ps_list.append(msg_str)
        alert_str = f"alert:{n}:wfs_models"
        trns_ps_list.append(alert_str)
    print(trns_ps_list)






if __name__=='__main__':
    complex_df_agg_type1()



