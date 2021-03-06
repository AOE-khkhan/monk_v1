import os
import sys
sys.path.append("../../../monk/");
import psutil

from gluon_prototype import prototype
from compare_prototype import compare
from common import print_start
from common import print_status

import numpy as np
from tf_keras_1.losses.return_loss import load_loss


def test_loss_l1(system_dict):
    forward = True;

    test = "test_loss_l1";
    system_dict["total_tests"] += 1;
    print_start(test, system_dict["total_tests"])
    if(forward):
        try:
            gtf = prototype(verbose=0);
            gtf.Prototype("sample-project-1", "sample-experiment-1");

            y = np.random.randn(1, 5);
            label = np.random.randn(1, 5);

            gtf.loss_l1();
            load_loss(gtf.system_dict);
            loss_obj = gtf.system_dict["local"]["criterion"];
            loss_val = loss_obj(label, y);           

            system_dict["successful_tests"] += 1;
            print_status("Pass");

        except Exception as e:
            system_dict["failed_tests_exceptions"].append(e);
            system_dict["failed_tests_lists"].append(test);
            forward = False;
            print_status("Fail");
    else:
        system_dict["skipped_tests_lists"].append(test);
        print_status("Skipped");

    return system_dict
