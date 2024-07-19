import configparser
import os

parser = configparser.ConfigParser()

# Construct the path relative to the current file
current_dir = os.path.dirname(os.path.abspath(__file__))
config_file_path = os.path.join(current_dir, "config.ini")

parser.read(config_file_path)


def get_cclf_1_column_spec() -> list:

    CCLF1_col_specification = [
        (0, 13),
        (13, 19),
        (19, 30),
        (30, 41),
        (41, 43),
        (43, 53),
        (53, 63),
        (63, 64),
        (64, 65),
        (65, 72),
        (72, 79),
        (79, 81),
        (81, 98),
        (98, 99),
        (99, 101),
        (101, 103),
        (103, 107),
        (107, 108),
        (108, 118),
        (118, 128),
        (128, 138),
        (138, 148),
        (148, 150),
        (150, 160),
        (160, 170),
        (170, 181),
        (181, 183),
        (183, 185),
        (185, 186),
        (186, 187),
        (187, 188),
        (188, 203),
        (203, 218),
        (218, 240),
        (240, 255),
        (255, 270),
        (270, 292),
        (292, 312),
        (312, 322),
        (322, 332),
        (332, 342),
        (342, 352),
    ]

    return CCLF1_col_specification


def get_cclf_2_column_spec() -> list:

    CCLF2_col_specification = [
        (0, 13),
        (13, 23),
        (23, 34),
        (34, 45),
        (45, 47),
        (47, 57),
        (57, 67),
        (67, 71),
        (71, 81),
        (81, 86),
        (86, 97),
        (97, 103),
        (103, 113),
        (113, 123),
        (123, 147),
        (147, 164),
        (164, 166),
        (166, 168),
        (168, 170),
        (170, 172),
        (172, 174),
        (174, 179),
        (179, 185),
    ]

    return CCLF2_col_specification


def get_cclf_3_column_spec() -> list:

    CCLF3_col_specification = [
        (0, 13),
        (13, 24),
        (24, 35),
        (35, 37),
        (37, 39),
        (39, 46),
        (46, 56),
        (56, 67),
        (67, 73),
        (73, 83),
        (83, 93),
        (93, 94),
    ]

    return CCLF3_col_specification


def get_cclf_4_column_spec() -> list:

    CCLF4_col_specification = [
        (0, 13),
        (13, 24),
        (24, 35),
        (35, 37),
        (37, 38),
        (38, 40),
        (40, 47),
        (47, 58),
        (58, 64),
        (64, 74),
        (74, 84),
        (84, 91),
        (91, 92),
        (92, 98),
    ]

    return CCLF4_col_specification


def get_cclf_5_column_spec() -> list:

    CCLF5_col_specification = [
        (0, 13),
        (13, 23),
        (23, 34),
        (34, 45),
        (45, 47),
        (47, 57),
        (57, 67),
        (67, 70),
        (70, 72),
        (72, 74),
        (74, 75),
        (75, 77),
        (77, 87),
        (87, 97),
        (97, 102),
        (102, 117),
        (117, 118),
        (118, 125),
        (125, 135),
        (135, 145),
        (145, 147),
        (147, 149),
        (149, 151),
        (151, 161),
        (161, 171),
        (171, 211),
        (211, 222),
        (222, 239),
        (239, 263),
        (263, 265),
        (265, 267),
        (267, 269),
        (269, 271),
        (271, 273),
        (273, 275),
        (275, 282),
        (282, 289),
        (289, 296),
        (296, 303),
        (303, 310),
        (310, 317),
        (317, 324),
        (324, 331),
        (331, 332),
        (332, 339),
        (339, 346),
        (346, 353),
        (353, 360),
        (360, 363),
        (363, 373),
        (373, 383),
    ]
    return CCLF5_col_specification


def get_cclf_6_column_spec() -> list:

    CCLF6_col_specification = [
        (0, 13),
        (13, 23),
        (23, 34),
        (34, 45),
        (45, 47),
        (47, 57),
        (57, 67),
        (67, 68),
        (68, 70),
        (70, 80),
        (80, 90),
        (90, 95),
        (95, 110),
        (110, 111),
        (111, 121),
        (121, 131),
        (131, 133),
        (133, 135),
        (135, 137),
        (137, 147),
        (147, 157),
        (157, 197),
        (197, 208),
        (208, 225),
        (225, 227),
        (227, 237),
        (237, 247),
    ]

    return CCLF6_col_specification


def get_cclf_7_column_spec() -> list:

    CCLF7_col_specification = [
        (0, 13),
        (13, 24),
        (24, 35),
        (35, 46),
        (46, 48),
        (48, 58),
        (58, 60),
        (60, 80),
        (80, 81),
        (81, 82),
        (82, 106),
        (106, 115),
        (115, 117),
        (117, 137),
        (137, 150),
        (150, 152),
        (152, 162),
        (162, 172),
        (172, 184),
        (184, 193),
        (193, 195),
    ]
    return CCLF7_col_specification


def get_cclf_8_column_spec() -> list:

    CCLF8_col_specification = [
        (0, 11),
        (11, 22),
        (22, 24),
        (24, 27),
        (27, 32),
        (32, 42),
        (42, 43),
        (43, 44),
        (44, 47),
        (47, 49),
        (49, 51),
        (51, 61),
        (61, 71),
        (71, 81),
        (81, 111),
        (111, 126),
        (126, 166),
        (166, 167),
        (167, 168),
        (168, 178),
        (178, 188),
        (188, 233),
        (233, 278),
        (278, 318),
        (318, 358),
        (358, 398),
        (398, 438),
        (438, 538),
        (538, 540),
        (540, 545),
        (545, 549),
    ]

    return CCLF8_col_specification


def get_cclf_9_column_spec() -> list:

    CCLF9_col_specification = [(0, 2), (2, 12), (12, 23), (23, 33), (33, 43), (43, 55)]

    return CCLF9_col_specification


def get_cclf_10_column_spec() -> list:

    CCLFA_col_specification = [
        (0, 13),
        (13, 24),
        (24, 35),
        (35, 37),
        (37, 47),
        (47, 48),
        (48, 49),
        (49, 50),
        (50, 51),
        (51, 52),
        (52, 54),
        (54, 56),
        (56, 58),
        (58, 60),
        (60, 62),
        (62, 81),
        (81, 100),
        (100, 101),
        (101, 120),
        (120, 135),
        (135, 154),
        (154, 169),
        (169, 184),
        (184, 203),
        (203, 222),
        (222, 224),
        (224, 243),
        (243, 262),
        (262, 281),
        (281, 300),
        (300, 303),
        (303, 305),
        (305, 324),
    ]

    return CCLFA_col_specification


def get_cclf_11_column_spec() -> list:

    CCLFB_col_specification = [
        (0, 13),
        (13, 23),
        (23, 34),
        (34, 45),
        (45, 47),
        (47, 48),
        (48, 49),
        (49, 50),
        (50, 51),
        (51, 52),
        (52, 54),
        (54, 56),
        (56, 58),
        (58, 60),
        (60, 62),
        (62, 77),
        (77, 92),
        (92, 93),
        (93, 112),
        (112, 127),
        (127, 128),
    ]

    return CCLFB_col_specification


# HEADERS


def get_cclf_0_header_names() -> list[str]:

    CCLF0_headers = [
        "File Number  ",
        "File Description    ",
        "Total Records Count ",
        "Record Length",
    ]

    return CCLF0_headers


def get_cclf_1_header_names() -> list[str]:

    CCLF1_headers = [
        "cur_clm_uniq_id",
        "prvdr_oscar_num",
        "bene_mbi_id",
        "bene_hic_num",
        "clm_type_cd",
        "clm_from_dt",
        "clm_thru_dt",
        "clm_bill_fac_type_cd",
        "clm_bill_clsfctn_cd",
        "prncpl_dgns_cd",
        "admtg_dgns_cd",
        "clm_mdcr_npmt_rsn_cd",
        "clm_pmt_amt",
        "clm_nch_prmry_pyr_cd",
        "prvdr_fac_fips_st_cd",
        "bene_ptnt_stus_cd",
        "dgns_drg_cd",
        "clm_op_srvc_type_cd",
        "fac_prvdr_npi_num",
        "oprtg_prvdr_npi_num",
        "atndg_prvdr_npi_num",
        "othr_prvdr_npi_num",
        "clm_adjsmt_type_cd",
        "clm_efctv_dt",
        "clm_idr_ld_dt",
        "bene_eqtbl_bic_hicn_num",
        "clm_admsn_type_cd",
        "clm_admsn_src_cd",
        "clm_bill_freq_cd",
        "clm_query_cd",
        "dgns_prcdr_icd_ind",
        "clm_mdcr_instnl_tot_chrg_amt",
        "clm_mdcr_ip_pps_cptl_ime_amt",
        "clm_oprtnl_ime_amt",
        "clm_mdcr_ip_pps_dsprprtnt_amt",
        "clm_hipps_uncompd_care_amt",
        "clm_oprtnl_dsprprtnt_amt",
        "clm_blg_prvdr_oscar_num",
        "clm_blg_prvdr_npi_num",
        "clm_oprtg_prvdr_npi_num",
        "clm_atndg_prvdr_npi_num",
        "clm_othr_prvdr_npi_num",
    ]

    return CCLF1_headers


def get_cclf_2_header_names() -> list[str]:

    CCLF2_headers = [
        "cur_clm_uniq_id",
        "clm_line_num",
        "bene_mbi_id",
        "bene_hic_num",
        "clm_type_cd",
        "clm_line_from_dt",
        "clm_line_thru_dt",
        "clm_line_prod_rev_ctr_cd",
        "clm_line_instnl_rev_ctr_dt",
        "clm_line_hcpcs_cd",
        "bene_eqtbl_bic_hicn_num",
        "prvdr_oscar_num",
        "clm_from_dt",
        "clm_thru_dt",
        "clm_line_srvc_unit_qty",
        "clm_line_cvrd_pd_amt",
        "hcpcs_1_mdfr_cd",
        "hcpcs_2_mdfr_cd",
        "hcpcs_3_mdfr_cd",
        "hcpcs_4_mdfr_cd",
        "hcpcs_5_mdfr_cd",
        "clm_rev_apc_hipps_cd",
        "clm_fac_prvdr_oscar_num",
    ]

    return CCLF2_headers


def get_cclf_3_header_names() -> list[str]:

    CCLF3_headers = [
        "cur_clm_uniq_id",
        "bene_mbi_id",
        "bene_hic_num",
        "clm_type_cd",
        "clm_val_sqnc_num",
        "clm_prcdr_cd",
        "clm_prcdr_prfrm_dt",
        "bene_eqtbl_bic_hicn_num",
        "prvdr_oscar_num",
        "clm_from_dt",
        "clm_thru_dt",
        "dgns_prcdr_icd_ind",
    ]

    return CCLF3_headers


def get_cclf_4_header_names() -> list[str]:

    CCLF4_headers = [
        "cur_clm_uniq_id",
        "bene_mbi_id",
        "bene_hic_num",
        "clm_type_cd",
        "clm_prod_type_cd",
        "clm_val_sqnc_num",
        "clm_dgns_cd",
        "bene_eqtbl_bic_hicn_num",
        "prvdr_oscar_num",
        "clm_from_dt",
        "clm_thru_dt",
        "clm_poa_ind",
        "dgns_prcdr_icd_ind",
        "clm_blg_prvdr_oscar_num",
    ]

    return CCLF4_headers


def get_cclf_5_header_names() -> list[str]:

    CCLF5_headers = [
        "cur_clm_uniq_id",
        "clm_line_num",
        "bene_mbi_id",
        "bene_hic_num",
        "clm_type_cd",
        "clm_from_dt",
        "clm_thru_dt",
        "rndrg_prvdr_type_cd",
        "rndrg_prvdr_fips_st_cd",
        "clm_prvdr_spclty_cd",
        "clm_fed_type_srvc_cd",
        "clm_pos_cd",
        "clm_line_from_dt",
        "clm_line_thru_dt",
        "clm_line_hcpcs_cd",
        "clm_line_cvrd_pd_amt",
        "clm_line_prmry_pyr_cd",
        "clm_line_dgns_cd",
        "clm_rndrg_prvdr_tax_num",
        "rndrg_prvdr_npi_num",
        "clm_carr_pmt_dnl_cd",
        "clm_prcsg_ind_cd",
        "clm_adjsmt_type_cd",
        "clm_efctv_dt",
        "clm_idr_ld_dt",
        "clm_cntl_num",
        "bene_eqtbl_bic_hicn_num",
        "clm_line_alowd_chrg_amt",
        "clm_line_srvc_unit_qty",
        "hcpcs_1_mdfr_cd",
        "hcpcs_2_mdfr_cd",
        "hcpcs_3_mdfr_cd",
        "hcpcs_4_mdfr_cd",
        "hcpcs_5_mdfr_cd",
        "clm_disp_cd",
        "clm_dgns_1_cd",
        "clm_dgns_2_cd",
        "clm_dgns_3_cd",
        "clm_dgns_4_cd",
        "clm_dgns_5_cd",
        "clm_dgns_6_cd",
        "clm_dgns_7_cd",
        "clm_dgns_8_cd",
        "dgns_prcdr_icd_ind",
        "clm_dgns_9_cd",
        "clm_dgns_10_cd",
        "clm_dgns_11_cd",
        "clm_dgns_12_cd",
        "hcpcs_betos_cd",
        "clm_rndrg_prvdr_npi_num",
        "clm_rfrg_prvdr_npi_num",
    ]

    return CCLF5_headers


def get_cclf_6_header_names() -> list[str]:

    CCLF6_headers = [
        "cur_clm_uniq_id",
        "clm_line_num",
        "bene_mbi_id",
        "bene_hic_num",
        "clm_type_cd",
        "clm_from_dt",
        "clm_thru_dt",
        "clm_fed_type_srvc_cd",
        "clm_pos_cd",
        "clm_line_from_dt",
        "clm_line_thru_dt",
        "clm_line_hcpcs_cd",
        "clm_line_cvrd_pd_amt",
        "clm__prmry_pyr_cd",
        "payto_prvdr_npi_num",
        "ordrg_prvdr_npi_num",
        "clm_carr_pmt_dnl_cd",
        "clm_prcsg_ind_cd",
        "clm_adjsmt_type_cd",
        "clm_efctv_dt",
        "clm_idr_ld_dt",
        "clm_cntl_num",
        "bene_eqtbl_bic_hicn_num",
        "clm_line_alowd_chrg_amt",
        "clm_disp_cd",
        "clm_blg_prvdr_npi_num",
        "clm_rfrg_prvdr_npi_num",
    ]

    return CCLF6_headers


def get_cclf_7_header_names() -> list[str]:

    CCLF7_headers = [
        "cur_clm_uniq_id",
        "bene_mbi_id",
        "bene_hic_num",
        "clm_line_ndc_cd",
        "clm_type_cd",
        "clm_line_from_dt",
        "prvdr_srvc_id_qlfyr_cd",
        "clm_srvc_prvdr_gnrc_id_num",
        "clm_dspnsng_stus_cd",
        "clm_daw_prod_slctn_cd",
        "clm_line_srvc_unit_qty",
        "clm_line_days_suply_qty",
        "prvdr_prsbng_id_qlfyr_cd",
        "clm_prsbng_prvdr_gnrc_id_num",
        "clm_line_bene_pmt_amt",
        "clm_adjsmt_type_cd",
        "clm_efctv_dt",
        "clm_idr_ld_dt",
        "clm_line_rx_srvc_rfrnc_num",
        "clm_line_rx_fill_num",
        "clm_phrmcy_srvc_type_cd",
    ]

    return CCLF7_headers


def get_cclf_8_header_names() -> list[str]:

    CCLF8_headers = [
        "bene_mbi_id",
        "bene_hic_num",
        "bene_fips_state_cd",
        "bene_fips_cnty_cd",
        "bene_zip_cd",
        "bene_dob",
        "bene_sex_cd",
        "bene_race_cd",
        "bene_age",
        "bene_mdcr_stus_cd",
        "bene_dual_stus_cd",
        "bene_death_dt",
        "bene_rng_bgn_dt",
        "bene_rng_end_dt",
        "bene_1st_name",
        "bene_midl_name",
        "bene_last_name",
        "bene_orgnl_entlmt_rsn_cd",
        "bene_entlmt_buyin_ind",
        "bene_part_a_enrlmt_bgn_dt",
        "bene_part_b_enrlmt_bgn_dt",
        "bene_line_1_adr",
        "bene_line_2_adr",
        "bene_line_3_adr",
        "bene_line_4_adr",
        "bene_line_5_adr",
        "bene_line_6_adr",
        "geo_zip_plc_name",
        "geo_usps_state_cd",
        "geo_zip5_cd",
        "geo_zip4_cd",
    ]

    return CCLF8_headers


def get_cclf_9_header_names() -> list[str]:

    CCLF9_headers = [
        "mbi_indicator",
        "crnt_num",
        "prvs_num",
        "prvs_id_efctv_dt",
        "prvs_id_obslt_dt",
        "benef_rrb_num",
    ]

    return CCLF9_headers


def get_cclf_10_header_names() -> list[str]:

    CCLFA_headers = [
        "cur_clm_uniq_id",
        "bene_mbi_id",
        "bene_hic_num",
        "clm_type_cd",
        "clm_actv_care_from_dt",
        "clm_ngaco_pbpmt_sw",
        "clm_ngaco_pdschrg_hcbs_sw",
        "clm_ngaco_snf_wvr_sw",
        "clm_ngaco_tlhlth_sw",
        "clm_ngaco_cptatn_sw",
        "clm_demo_1st_num",
        "clm_demo_2nd_num",
        "clm_demo_3rd_num",
        "clm_demo_4th_num",
        "clm_demo_5th_num",
        "clm_pbp_inclsn_amt",
        "clm_pbp_rdctn_amt",
        "clm_ngaco_cmg_wvr_sw",
        "clm_instnl_per_diem_amt",
        "clm_mdcr_ip_bene_ddctbl_amt",
        "clm_mdcr_coinsrnc_amt",
        "clm_blood_lblty_amt",
        "clm_instnl_prfnl_amt",
        "clm_ncvrd_chrg_amt",
        "clm_mdcr_ddctbl_amt",
        "clm_rlt_cond_cd",
        "clm_oprtnl_outlr_amt",
        "clm_mdcr_new_tech_amt",
        "clm_islet_isoln_amt",
        "clm_sqstrtn_rdctn_amt",
        "clm_1_rev_cntr_ansi_rsn_cd",
        "clm_1_rev_cntr_ansi_grp_cd",
        "clm_mips_pmt_amt",
    ]

    return CCLFA_headers


def get_cclf_11_header_names() -> list[str]:

    CCLFB_headers = [
        "cur_clm_uniq_id",
        "clm_line_num",
        "bene_mbi_id",
        "bene_hic_num",
        "clm_type_cd",
        "clm_line_ngaco_pbpmt_sw",
        "clm_line_ngaco_pdschrg_hcbs_sw",
        "clm_line_ngaco_snf_wvr_sw",
        "clm_line_ngaco_tlhlth_sw",
        "clm_line_ngaco_cptatn_sw",
        "clm_demo_1st_num",
        "clm_demo_2nd_num",
        "clm_demo_3rd_num",
        "clm_demo_4th_num",
        "clm_demo_5th_num",
        "clm_pbp_inclsn_amt",
        "clm_pbp_rdctn_amt",
        "clm_ngaco_cmg_wvr_sw",
        "clm_mdcr_ddctbl_amt",
        "clm_sqstrtn_rdctn_amt",
        "clm_line_carr_hpsa_scrcty_cd",
    ]

    return CCLFB_headers
