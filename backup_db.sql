PGDMP      '                |           ping    16.3    16.3     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    16397    ping    DATABASE     y   CREATE DATABASE ping WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Russian_Ukraine.1251';
    DROP DATABASE ping;
                postgres    false            �           0    0    DATABASE ping    ACL     e   REVOKE ALL ON DATABASE ping FROM postgres;
GRANT ALL ON DATABASE ping TO postgres WITH GRANT OPTION;
                   postgres    false    4784            �            1259    16398    users    TABLE     �   CREATE TABLE public.users (
    id bigint NOT NULL,
    name text NOT NULL,
    surname text NOT NULL,
    lastname text NOT NULL,
    user_group text NOT NULL,
    group_id text NOT NULL
);
    DROP TABLE public.users;
       public         heap    postgres    false            �            1259    16409    users_id_seq    SEQUENCE     �   ALTER TABLE public.users ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.users_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);
            public          postgres    false    215                       2606    16408    users users_pkey 
   CONSTRAINT     N   ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);
 :   ALTER TABLE ONLY public.users DROP CONSTRAINT users_pkey;
       public            postgres    false    215           