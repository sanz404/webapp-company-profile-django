# Generated by Django 3.2.7 on 2022-07-23 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0007_auto_20220723_0744'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='article',
            index=models.Index(fields=['user_id'], name='api_app_art_user_id_67a9b4_idx'),
        ),
        migrations.AddIndex(
            model_name='article',
            index=models.Index(fields=['image'], name='api_app_art_image_4eb40d_idx'),
        ),
        migrations.AddIndex(
            model_name='article',
            index=models.Index(fields=['slug'], name='api_app_art_slug_1d1ad0_idx'),
        ),
        migrations.AddIndex(
            model_name='article',
            index=models.Index(fields=['title'], name='api_app_art_title_426dbf_idx'),
        ),
        migrations.AddIndex(
            model_name='article',
            index=models.Index(fields=['is_published'], name='api_app_art_is_publ_cf2895_idx'),
        ),
        migrations.AddIndex(
            model_name='article',
            index=models.Index(fields=['created_at'], name='api_app_art_created_e37c99_idx'),
        ),
        migrations.AddIndex(
            model_name='article',
            index=models.Index(fields=['updated_at'], name='api_app_art_updated_e30edf_idx'),
        ),
        migrations.AddIndex(
            model_name='categoryarticle',
            index=models.Index(fields=['name'], name='api_app_cat_name_a1a869_idx'),
        ),
        migrations.AddIndex(
            model_name='categoryarticle',
            index=models.Index(fields=['created_at'], name='api_app_cat_created_3c3e8d_idx'),
        ),
        migrations.AddIndex(
            model_name='categoryarticle',
            index=models.Index(fields=['updated_at'], name='api_app_cat_updated_009564_idx'),
        ),
        migrations.AddIndex(
            model_name='categoryfaq',
            index=models.Index(fields=['name'], name='api_app_cat_name_6be9b8_idx'),
        ),
        migrations.AddIndex(
            model_name='categoryfaq',
            index=models.Index(fields=['created_at'], name='api_app_cat_created_9a7539_idx'),
        ),
        migrations.AddIndex(
            model_name='categoryfaq',
            index=models.Index(fields=['updated_at'], name='api_app_cat_updated_7ec134_idx'),
        ),
        migrations.AddIndex(
            model_name='categoryproduct',
            index=models.Index(fields=['name'], name='api_app_cat_name_ef0792_idx'),
        ),
        migrations.AddIndex(
            model_name='categoryproduct',
            index=models.Index(fields=['created_at'], name='api_app_cat_created_955975_idx'),
        ),
        migrations.AddIndex(
            model_name='categoryproduct',
            index=models.Index(fields=['updated_at'], name='api_app_cat_updated_5812d1_idx'),
        ),
        migrations.AddIndex(
            model_name='categoryproject',
            index=models.Index(fields=['name'], name='api_app_cat_name_2bdf13_idx'),
        ),
        migrations.AddIndex(
            model_name='categoryproject',
            index=models.Index(fields=['created_at'], name='api_app_cat_created_9bc316_idx'),
        ),
        migrations.AddIndex(
            model_name='categoryproject',
            index=models.Index(fields=['updated_at'], name='api_app_cat_updated_667f8c_idx'),
        ),
        migrations.AddIndex(
            model_name='contact',
            index=models.Index(fields=['name'], name='api_app_con_name_db6760_idx'),
        ),
        migrations.AddIndex(
            model_name='contact',
            index=models.Index(fields=['email'], name='api_app_con_email_a597af_idx'),
        ),
        migrations.AddIndex(
            model_name='contact',
            index=models.Index(fields=['phone'], name='api_app_con_phone_5cafcc_idx'),
        ),
        migrations.AddIndex(
            model_name='contact',
            index=models.Index(fields=['website'], name='api_app_con_website_a06cb0_idx'),
        ),
        migrations.AddIndex(
            model_name='contact',
            index=models.Index(fields=['created_at'], name='api_app_con_created_e41643_idx'),
        ),
        migrations.AddIndex(
            model_name='contact',
            index=models.Index(fields=['updated_at'], name='api_app_con_updated_044fd0_idx'),
        ),
        migrations.AddIndex(
            model_name='content',
            index=models.Index(fields=['key_name'], name='api_app_con_key_nam_594b1b_idx'),
        ),
        migrations.AddIndex(
            model_name='content',
            index=models.Index(fields=['created_at'], name='api_app_con_created_ef65d1_idx'),
        ),
        migrations.AddIndex(
            model_name='content',
            index=models.Index(fields=['updated_at'], name='api_app_con_updated_72e594_idx'),
        ),
        migrations.AddIndex(
            model_name='country',
            index=models.Index(fields=['code'], name='api_app_cou_code_533515_idx'),
        ),
        migrations.AddIndex(
            model_name='country',
            index=models.Index(fields=['name'], name='api_app_cou_name_f41fd7_idx'),
        ),
        migrations.AddIndex(
            model_name='country',
            index=models.Index(fields=['created_at'], name='api_app_cou_created_9c75fc_idx'),
        ),
        migrations.AddIndex(
            model_name='country',
            index=models.Index(fields=['updated_at'], name='api_app_cou_updated_627808_idx'),
        ),
        migrations.AddIndex(
            model_name='emailverification',
            index=models.Index(fields=['user_id'], name='api_app_ema_user_id_b6d22a_idx'),
        ),
        migrations.AddIndex(
            model_name='emailverification',
            index=models.Index(fields=['code'], name='api_app_ema_code_d15b9d_idx'),
        ),
        migrations.AddIndex(
            model_name='emailverification',
            index=models.Index(fields=['token'], name='api_app_ema_token_f6aa7a_idx'),
        ),
        migrations.AddIndex(
            model_name='emailverification',
            index=models.Index(fields=['email_confirmed'], name='api_app_ema_email_c_1dbdeb_idx'),
        ),
        migrations.AddIndex(
            model_name='emailverification',
            index=models.Index(fields=['is_expired'], name='api_app_ema_is_expi_7bd010_idx'),
        ),
        migrations.AddIndex(
            model_name='emailverification',
            index=models.Index(fields=['expired_at'], name='api_app_ema_expired_0decaa_idx'),
        ),
        migrations.AddIndex(
            model_name='emailverification',
            index=models.Index(fields=['created_at'], name='api_app_ema_created_7c39ec_idx'),
        ),
        migrations.AddIndex(
            model_name='emailverification',
            index=models.Index(fields=['updated_at'], name='api_app_ema_updated_b8cc85_idx'),
        ),
        migrations.AddIndex(
            model_name='faq',
            index=models.Index(fields=['category_id'], name='api_app_faq_categor_3c4de0_idx'),
        ),
        migrations.AddIndex(
            model_name='faq',
            index=models.Index(fields=['question'], name='api_app_faq_questio_090978_idx'),
        ),
        migrations.AddIndex(
            model_name='faq',
            index=models.Index(fields=['sort'], name='api_app_faq_sort_8890a1_idx'),
        ),
        migrations.AddIndex(
            model_name='faq',
            index=models.Index(fields=['is_published'], name='api_app_faq_is_publ_e1ac31_idx'),
        ),
        migrations.AddIndex(
            model_name='faq',
            index=models.Index(fields=['created_at'], name='api_app_faq_created_ac5ed7_idx'),
        ),
        migrations.AddIndex(
            model_name='faq',
            index=models.Index(fields=['updated_at'], name='api_app_faq_updated_a944f1_idx'),
        ),
        migrations.AddIndex(
            model_name='feature',
            index=models.Index(fields=['icon'], name='api_app_fea_icon_a344b0_idx'),
        ),
        migrations.AddIndex(
            model_name='feature',
            index=models.Index(fields=['title'], name='api_app_fea_title_9f9502_idx'),
        ),
        migrations.AddIndex(
            model_name='feature',
            index=models.Index(fields=['is_published'], name='api_app_fea_is_publ_47a944_idx'),
        ),
        migrations.AddIndex(
            model_name='feature',
            index=models.Index(fields=['created_at'], name='api_app_fea_created_e45598_idx'),
        ),
        migrations.AddIndex(
            model_name='feature',
            index=models.Index(fields=['updated_at'], name='api_app_fea_updated_b2c127_idx'),
        ),
        migrations.AddIndex(
            model_name='message',
            index=models.Index(fields=['full_name'], name='api_app_mes_full_na_a9e55d_idx'),
        ),
        migrations.AddIndex(
            model_name='message',
            index=models.Index(fields=['email'], name='api_app_mes_email_528cc7_idx'),
        ),
        migrations.AddIndex(
            model_name='message',
            index=models.Index(fields=['phone'], name='api_app_mes_phone_aa1673_idx'),
        ),
        migrations.AddIndex(
            model_name='message',
            index=models.Index(fields=['created_at'], name='api_app_mes_created_12d829_idx'),
        ),
        migrations.AddIndex(
            model_name='message',
            index=models.Index(fields=['updated_at'], name='api_app_mes_updated_37e588_idx'),
        ),
        migrations.AddIndex(
            model_name='notiifcation',
            index=models.Index(fields=['user_id'], name='api_app_not_user_id_b6ea5d_idx'),
        ),
        migrations.AddIndex(
            model_name='notiifcation',
            index=models.Index(fields=['subject'], name='api_app_not_subject_90a08b_idx'),
        ),
        migrations.AddIndex(
            model_name='notiifcation',
            index=models.Index(fields=['sort_content'], name='api_app_not_sort_co_509e6f_idx'),
        ),
        migrations.AddIndex(
            model_name='notiifcation',
            index=models.Index(fields=['readed_at'], name='api_app_not_readed__f67df9_idx'),
        ),
        migrations.AddIndex(
            model_name='notiifcation',
            index=models.Index(fields=['created_at'], name='api_app_not_created_9f484d_idx'),
        ),
        migrations.AddIndex(
            model_name='notiifcation',
            index=models.Index(fields=['updated_at'], name='api_app_not_updated_ec324a_idx'),
        ),
        migrations.AddIndex(
            model_name='person',
            index=models.Index(fields=['user_id'], name='api_app_per_user_id_e8bbf8_idx'),
        ),
        migrations.AddIndex(
            model_name='person',
            index=models.Index(fields=['phone'], name='api_app_per_phone_5fcb35_idx'),
        ),
        migrations.AddIndex(
            model_name='person',
            index=models.Index(fields=['city'], name='api_app_per_city_05b211_idx'),
        ),
        migrations.AddIndex(
            model_name='person',
            index=models.Index(fields=['zip_code'], name='api_app_per_zip_cod_af48e7_idx'),
        ),
        migrations.AddIndex(
            model_name='person',
            index=models.Index(fields=['is_admin'], name='api_app_per_is_admi_102399_idx'),
        ),
        migrations.AddIndex(
            model_name='person',
            index=models.Index(fields=['status'], name='api_app_per_status_9adf85_idx'),
        ),
        migrations.AddIndex(
            model_name='person',
            index=models.Index(fields=['created_at'], name='api_app_per_created_c9e9f3_idx'),
        ),
        migrations.AddIndex(
            model_name='person',
            index=models.Index(fields=['updated_at'], name='api_app_per_updated_acb6fb_idx'),
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['category_id'], name='api_app_pro_categor_61ab32_idx'),
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['name'], name='api_app_pro_name_e3fd63_idx'),
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['image'], name='api_app_pro_image_2fffdf_idx'),
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['price'], name='api_app_pro_price_596817_idx'),
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['is_published'], name='api_app_pro_is_publ_da0d12_idx'),
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['created_at'], name='api_app_pro_created_acbab5_idx'),
        ),
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['updated_at'], name='api_app_pro_updated_b6621f_idx'),
        ),
        migrations.AddIndex(
            model_name='project',
            index=models.Index(fields=['category_id'], name='api_app_pro_categor_3c0182_idx'),
        ),
        migrations.AddIndex(
            model_name='project',
            index=models.Index(fields=['name'], name='api_app_pro_name_5737e5_idx'),
        ),
        migrations.AddIndex(
            model_name='project',
            index=models.Index(fields=['image'], name='api_app_pro_image_2990ec_idx'),
        ),
        migrations.AddIndex(
            model_name='project',
            index=models.Index(fields=['is_published'], name='api_app_pro_is_publ_f87d6e_idx'),
        ),
        migrations.AddIndex(
            model_name='project',
            index=models.Index(fields=['created_at'], name='api_app_pro_created_1a7080_idx'),
        ),
        migrations.AddIndex(
            model_name='project',
            index=models.Index(fields=['updated_at'], name='api_app_pro_updated_fe49e4_idx'),
        ),
        migrations.AddIndex(
            model_name='team',
            index=models.Index(fields=['name'], name='api_app_tea_name_426e54_idx'),
        ),
        migrations.AddIndex(
            model_name='team',
            index=models.Index(fields=['image'], name='api_app_tea_image_094418_idx'),
        ),
        migrations.AddIndex(
            model_name='team',
            index=models.Index(fields=['position'], name='api_app_tea_positio_6f56e4_idx'),
        ),
        migrations.AddIndex(
            model_name='team',
            index=models.Index(fields=['is_published'], name='api_app_tea_is_publ_ad4c58_idx'),
        ),
        migrations.AddIndex(
            model_name='team',
            index=models.Index(fields=['created_at'], name='api_app_tea_created_57e595_idx'),
        ),
        migrations.AddIndex(
            model_name='team',
            index=models.Index(fields=['updated_at'], name='api_app_tea_updated_c86a7d_idx'),
        ),
    ]
