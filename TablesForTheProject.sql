PGDMP         %             	    y           Data    12.8    12.6     a           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            b           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            c           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            d           1262    16416    Data    DATABASE     d   CREATE DATABASE "Data" WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'C' LC_CTYPE = 'C';
    DROP DATABASE "Data";
                postgres    false                        2615    16417 
   StudyGroup    SCHEMA        CREATE SCHEMA "StudyGroup";
    DROP SCHEMA "StudyGroup";
                postgres    false            ?            1259    16427 
   Assignment    TABLE     ,   CREATE TABLE "StudyGroup"."Assignment" (
);
 &   DROP TABLE "StudyGroup"."Assignment";
    
   StudyGroup         heap    postgres    false    7            ?            1259    16424    Course    TABLE     (   CREATE TABLE "StudyGroup"."Course" (
);
 "   DROP TABLE "StudyGroup"."Course";
    
   StudyGroup         heap    postgres    false    7            ?            1259    16433    In Person Meeting    TABLE     3   CREATE TABLE "StudyGroup"."In Person Meeting" (
);
 -   DROP TABLE "StudyGroup"."In Person Meeting";
    
   StudyGroup         heap    postgres    false    7            ?            1259    16430    Meeting    TABLE     )   CREATE TABLE "StudyGroup"."Meeting" (
);
 #   DROP TABLE "StudyGroup"."Meeting";
    
   StudyGroup         heap    postgres    false    7            ?            1259    16436    Online Meeting    TABLE     0   CREATE TABLE "StudyGroup"."Online Meeting" (
);
 *   DROP TABLE "StudyGroup"."Online Meeting";
    
   StudyGroup         heap    postgres    false    7            ?            1259    16421    Section    TABLE     )   CREATE TABLE "StudyGroup"."Section" (
);
 #   DROP TABLE "StudyGroup"."Section";
    
   StudyGroup         heap    postgres    false    7            ?            1259    16418    Student    TABLE     )   CREATE TABLE "StudyGroup"."Student" (
);
 #   DROP TABLE "StudyGroup"."Student";
    
   StudyGroup         heap    postgres    false    7            ?            1259    16439    Study_Group    TABLE     -   CREATE TABLE "StudyGroup"."Study_Group" (
);
 '   DROP TABLE "StudyGroup"."Study_Group";
    
   StudyGroup         heap    postgres    false    7            Z          0    16427 
   Assignment 
   TABLE DATA           ,   COPY "StudyGroup"."Assignment"  FROM stdin;
 
   StudyGroup          postgres    false    206   ?       Y          0    16424    Course 
   TABLE DATA           (   COPY "StudyGroup"."Course"  FROM stdin;
 
   StudyGroup          postgres    false    205   ?       \          0    16433    In Person Meeting 
   TABLE DATA           3   COPY "StudyGroup"."In Person Meeting"  FROM stdin;
 
   StudyGroup          postgres    false    208          [          0    16430    Meeting 
   TABLE DATA           )   COPY "StudyGroup"."Meeting"  FROM stdin;
 
   StudyGroup          postgres    false    207   5       ]          0    16436    Online Meeting 
   TABLE DATA           0   COPY "StudyGroup"."Online Meeting"  FROM stdin;
 
   StudyGroup          postgres    false    209   R       X          0    16421    Section 
   TABLE DATA           )   COPY "StudyGroup"."Section"  FROM stdin;
 
   StudyGroup          postgres    false    204   o       W          0    16418    Student 
   TABLE DATA           )   COPY "StudyGroup"."Student"  FROM stdin;
 
   StudyGroup          postgres    false    203   ?       ^          0    16439    Study_Group 
   TABLE DATA           -   COPY "StudyGroup"."Study_Group"  FROM stdin;
 
   StudyGroup          postgres    false    210   ?       Z      x?????? ? ?      Y      x?????? ? ?      \      x?????? ? ?      [      x?????? ? ?      ]      x?????? ? ?      X      x?????? ? ?      W      x?????? ? ?      ^      x?????? ? ?     