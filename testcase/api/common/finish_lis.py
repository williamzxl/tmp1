from testcase.api.studyCenter.sysListening.all_listening_interface import AllListenInterface


def finish_lis(task, common, headers, access_token):
    print("*" * 80)
    if task.get('currStatus') == 0 or task.get('currStatus') == 1:
        practiceType = task.get("practiceType")
        currStatus = task.get("currStatus")
        taskID = task.get("taskID")
        groupID = task.get("groupID")
        # print(practiceType, currStatus, taskID, groupID)
        if currStatus == 0:
            if practiceType == 1:
                # print(practiceType, currStatus, taskID, groupID)
                word_listen = AllListenInterface(common, headers, access_token)
                word_listen_answers = word_listen.get_all_dict_answer(groupID, taskID)
                for answer in word_listen_answers:
                    post_word_dict_answer = word_listen.post_all_word_dict_answer(taskID, answer)
                word_dict_words = word_listen.get_word_dict_words(groupID, taskID, practiceType)
                wd_words = word_listen.get_word_dict_words(groupID, taskID, practiceType)
                for star in wd_words:
                    r = word_listen.put_word_dict_words(star)
            if practiceType == 2:
                # print(practiceType, currStatus, taskID, groupID)
                word_trans_get = AllListenInterface(common, headers, access_token)
                word_trans_answers = word_trans_get.get_all_word_tran_answer(groupID, taskID)
                for answer in word_trans_answers:
                    post_word_trans_answer = word_trans_get.post_all_word_tran_answer(taskID, answer)
                word_trans_words = word_trans_get.get_word_trans_words(groupID, taskID, practiceType)
                wt_words = word_trans_get.get_word_trans_words(groupID, taskID, practiceType)
                for star in wt_words:
                    # print(star)
                    r = word_trans_get.put_word_tran_words(star)
                    # print(r)
            if practiceType == 3:
                sen_fill = AllListenInterface(common, headers, access_token)
                sen_fill_answers = sen_fill.get_all_sen_fill_answer(groupID, taskID)
                for answer in sen_fill_answers:
                    # print("Answer", answer)
                    post_sen_fill_answer = sen_fill.post_all_sen_fill_answer(taskID, answer)
                sen_fill_words = sen_fill.get_sen_fill_words(groupID, taskID, practiceType)
                sf_words = sen_fill.get_sen_fill_words(groupID, taskID, practiceType)
                for star in sf_words:
                    r = sen_fill.put_sen_fill_words(star)
                sf_done_data = sen_fill.get_sen_fill_done_data(groupID, practiceType)
                sen_fill.put_sen_fill_done(sf_done_data, taskID)
        if currStatus == 1:
            word_lists_to_3start = AllListenInterface(common, headers, access_token)
            if practiceType == 1:
                word_dict_words = word_lists_to_3start.get_word_dict_words(groupID, taskID, practiceType)
                wd_words = word_lists_to_3start.get_word_trans_words(groupID, taskID, practiceType)
                for star in wd_words:
                    if star.get("oldF") == 3:
                        pass
                    else:
                        word_lists_to_3start.put_word_tran_words(star)
            if practiceType == 2:
                word_trans_words = word_lists_to_3start.get_word_trans_words(groupID, taskID,
                                                                             practiceType)
                wt_words = word_lists_to_3start.get_word_trans_words(groupID, taskID, practiceType)
                for star in wt_words:
                    if star.get("oldF") == 3:
                        pass
                    else:
                        word_lists_to_3start.put_word_tran_words(star)
            if practiceType == 3:
                sen_fill_words = word_lists_to_3start.get_sen_fill_words(groupID, taskID,
                                                                         practiceType)
                sf_words = word_lists_to_3start.get_sen_fill_words(groupID, taskID, practiceType)
                for star in sf_words:
                    if star.get("oldF") == 3:
                        pass
                    else:
                        print("+++++++++++++++++++++", star)
                        word_lists_to_3start.put_sen_fill_words(star)