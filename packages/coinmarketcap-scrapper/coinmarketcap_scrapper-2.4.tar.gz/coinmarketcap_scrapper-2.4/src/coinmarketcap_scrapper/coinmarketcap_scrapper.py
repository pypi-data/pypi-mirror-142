#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2022/01/01 20:23:55.455964
#+ Editado:	2022/03/10 23:45:20.389917
# ------------------------------------------------------------------------------
from typing import Optional, List, Union, Tuple
from bs4 import BeautifulSoup as bs
from math import ceil
from Levenshtein import distance
from datetime import datetime
import sqlite3
import sys
import os

from conexions import Proxy

from .excepcions import ErroTipado, ErroPaxinaInaccesibel
from .cmc_uteis import lazy_check_types

from .__variables import RAIZ
# ------------------------------------------------------------------------------

# xFCR: crear un ficheiro temporal para que se fai varias request moi seguidas non moleste á paxina
class CoinMarketCap:
    # atributos de clase
    __pax: int = 1
    __url: str = 'https://coinmarketcap.com'

    # Constructor --------------------------------------------------------------
    def __init__(self, verbose: bool = False, timeout: int = 10, reintentos: int = 5) -> None:
        # variables da instancia
        self.__pax = self.__pax
        self.__url = self.__url

        self.r = Proxy(verbose= verbose)
        self.r.set_timeout(timeout)
        self.r.set_reintentos(reintentos)
    # --------------------------------------------------------------------------

    # Getters ------------------------------------------------------------------

    def __get_from_db(self, sentenza, todos = True) -> Tuple[str]:
        # se mete mal o tipo dos valores saca erro
        if not lazy_check_types(todos, bool):
            raise ErroTipado('O tipo da "todos" non entra dentro do esperado (bool)')

        con = sqlite3.connect(os.path.join(RAIZ, 'ligazons.db'))
        cur = con.cursor()

        if todos:
            resultado = cur.execute(sentenza).fetchall()
        else:
            resultado = cur.execute(sentenza).fetchone()

        con.close()

        return resultado

    def get_pax(self) -> int:
        return self.__pax

    def get_url(self) -> str:
        return self.__url

    def get_url_pax(self, nova_pax: Optional[int] = 0) -> str:
        return self.__url+'/?page='+str(nova_pax)

    def get_reintentos(self) -> int:
        """
        """

        return self.r.get_reintentos()

    def get_timeout(self) -> int:
        """
        """

        return self.r.get_timeout()

    def get_verbose(self) -> bool:
        """
        """

        return self.r.get_verbose()

    # --------------------------------------------------------------------------

    # Setters ------------------------------------------------------------------

    def set_pax(self, nova_pax: int) -> None:
        self.__pax = nova_pax

    def set_reintentos(self, nova_cant_reintentos: int) -> None:
        """
        """

        self.r.set_reintentos(nova_cant_reintentos)

    def set_timeout(self, novo_timeout: int) -> None:
        """
        """

        self.r.set_timeout(novo_timeout)

    def set_verbose(self, novo_verbose: Union[int, bool]) -> None:
        """
        """

        self.r.set_verbose(novo_verbose)

    # --------------------------------------------------------------------------

    # get_info
    def get_info(self, reintentos: int = 0) -> dict:
        """
        Devolve a info xeral sobre o mercado.

        @entradas:
            Ningunha.

        @saídas:
            Dicionario  -   Sempre
            └ Cos datos que proporciona a páxina.
        """

        dic_info = {}
        dic_domin = {}

        if reintentos != 0:
            self.set_reintentos(reintentos)

        pax_web = self.r.get(self.get_url())

        if pax_web.status_code == 404:
            raise ErroPaxinaInaccesibel

        soup = bs(pax_web.text, 'html.parser')

        # devolve os resultados dúas veces, non sei por que
        info = soup.find_all(class_='sc-2bz68i-0')

        for ele in info[:int(len(info)/2)]:
            parte = ele.text.split(u': \xa0')
            dic_info[parte[0]] = parte[1]


        for ele in [ele.split(':') for ele in dic_info['Dominance'].split(u'\xa0')]:
            dic_domin[ele[0]] = ele[1]

        dic_info['Dominance'] = dic_domin

        return dic_info

    # get_top
    def get_top(self, topx: Optional[int] = 10, reintentos: int = 0) -> List[dict]:
        """
        Devolve o top de moedas en CoinMarketCap.

        @entradas:
            topx    -   Opcional    -   Enteiro
            └ Cantidade de moedas no top.

        @saídas:
            Lista de dicionarios  -   Sempre
            └ Cos datos pedidos.
        """

        # se mete mal o tipo dos valores saca erro
        if not lazy_check_types(topx, int):
            raise ErroTipado('O tipo da variable non entra dentro do esperado (int)')

        pasados = 0
        pax = 1
        lista_top = []
        tope = topx

        if reintentos != 0:
            self.set_reintentos(reintentos)

        #while pax<=ceil(topx/100):
        while True:
            try:
                pax_web = self.r.get(self.get_url_pax(pax))

                soup = bs(pax_web.text, 'html.parser')

                if (pax_web.status_code == 404) or (soup.find(class_='sc-404__StyledError-ic5ef7-0')):
                    raise ErroPaxinaInaccesibel

                taboa = soup.find('table').tbody.find_all('tr')

                xpax = len(taboa)

                for indice, fila in enumerate(taboa, 1):
                    # simbolo
                    try:
                        simbolo = fila.find(class_='crypto-symbol').text
                    except:
                        try:
                            simbolo = fila.find(class_='coin-item-symbol').text
                        except Exception as e:
                            raise Exception(e)
                    # simbolo #

                    # ligazon
                    try:
                        ligazon = fila.find(class_='cmc-link').get('href')
                    except Exception as e:
                        raise Exception(e)
                    # ligazon #

                    # prezo
                    try:
                        prezo = fila.find_all('td')[3].text
                    except Exception as e:
                        raise Exception(e)
                    # prezo #

                    # divisa
                    try:
                        divisa = prezo[0]
                    except Exception as e:
                        raise Exception(e)
                    # divisa #

                    # prezo
                    try:
                        prezo = prezo[1:]
                    except Exception as e:
                        raise Exception(e)
                    # prezo #

                    # nome
                    try:
                        nome = fila.find_all('td')[2].text
                        if nome.endswith('Buy'):
                            nome = nome[:-3]

                        if nome.endswith(simbolo):
                            nome = nome[:-len(simbolo)]

                        # podería dar problema se fose algo tipo Moeda1 o nome
                        if not nome.isdigit():
                            while nome[-1].isdigit():
                                nome = nome[:-1]
                    except Exception as e:
                        raise Exception(e)
                    # nome #

                    lista_top.append({
                        'posicion': indice+pasados,
                        'simbolo': simbolo,
                        'nome': nome,
                        'prezo': prezo,
                        'divisa': divisa,
                        'ligazon': ligazon
                        })

                pax+=1
                pasados += xpax

                # aki en lugar de no while pq asi podo sacar o xpax sen
                # outro request idiota ou recursión
                #if (pax>ceil(topx/xpax)) and (topx!=0):
                if (topx!=0) and (pasados>=topx):
                    lista_top = lista_top[:topx]
                    break
            # se peta saese do bucle
            except:
                break

        return lista_top

    @staticmethod
    def __mais_menos(terce: str) -> str:
        """
        """

        if 'down' in str(terce):
            return '-'
        return '+'

    @staticmethod
    def __fora_extras(texto: str, divisa_ref: str = None) -> str:
        """
        """

        if divisa_ref:
            return texto.replace(',','').replace(divisa_ref,'')
        return texto.replace(',','')

    # xFCRF devolve soamente usd, molaría para o futuro implementar outras
    # get_moeda
    def get_moeda(self, buscado: str, xvalor: Optional[str] = 'nome', reintentos: int = 0) -> dict:
        """
        Devolve toda a información posible sobre a moeda inquirida.

        @entradas:
            buscado -   Requirido   -   Catex
            └ Cadea de texto buscada.
            xvalor  -   Opcional    -   Catex
            └ Indica se quere que se busque como nome de moeda ou simbolo.

        @saídas:
            Dicionario  -   Sempre
            └ Con tódolos datos posibles.
        """

        # se mete mal o tipo dos valores saca erro
        if not lazy_check_types([buscado, xvalor, reintentos], [str, str, int]):
            raise ErroTipado('O tipo da variable non entra dentro do esperado (str)')

        CHAR_NULL = None

        if reintentos != 0:
            self.set_reintentos(reintentos)

        # se mete un campo raro busca por nome
        if xvalor not in ['nome', 'simbolo', 'ligazon']:
            xvalor = 'nome'

        buscado_sentenza = '%'.join(list(buscado))
        sentenza = f'select id, {xvalor} from moeda where {xvalor} like "%{buscado_sentenza}%"'
        busqueda = self.__get_from_db(sentenza)

        # non atopou ningún
        if len(busqueda) == 0:
            return {}

        id_buscado = 0
        min_distancia = sys.maxsize
        for moeda in busqueda:
            distancia = distance(buscado, moeda[1])
            if distancia<min_distancia:
                min_distancia = distancia
                id_buscado = moeda[0]

        obx_buscado = self.__get_from_db(f'select simbolo, nome, ligazon from moeda where id={id_buscado}', todos=False)

        pax_web = self.r.get(self.get_url()+obx_buscado[2])

        if pax_web.status_code == 404:
            raise ErroPaxinaInaccesibel

        soup = bs(pax_web.text, 'html.parser')

        datos = []
        for taboa in soup.find_all('table'):
            for ele in taboa.find_all('td'):
                datos.append(ele)

        # scraping
        # divisa_ref
        divisa_ref = datos[0].text[0]
        # prezo
        prezo = self.__fora_extras(datos[0].text, divisa_ref)
        # price_change
        try:
            prime, secon, terce = datos[1].find_all('span')
            price_change_24h = self.__fora_extras(prime.text, divisa_ref)
            price_change_pctx_24h = self.__mais_menos(terce)+secon.text
        except:
            price_change_24h = CHAR_NULL
            price_change_pctx_24h = CHAR_NULL
        # min/max 24h
        if datos[2].text != 'No Data':
            max_24h, min_24h = [ele.rstrip() for ele in self.__fora_extras(datos[2].text, divisa_ref).split('/')]
        else:
            max_24h = min_24h = CHAR_NULL
        # trading volume 24h
        try:
            prime, secon, terce = datos[3].find_all('span')
            trading_volume_24h = self.__fora_extras(prime.text, divisa_ref)
            trading_volume_change_pctx_24h = self.__mais_menos(terce)+secon.text
        except:
            trading_volume_24h = CHAR_NULL
            trading_volume_change_pctx_24h = CHAR_NULL
        # volume / market cap
        volume_dividido_market_cap = datos[4].text
        # dominancia mercado
        dominancia_mercado = datos[5].text
        # rango
        rango = datos[6].text

        # total value locked tvl
        if len(datos) >= 48:
            total_value_locked = self.__fora_extras(datos.pop(7).text)
        else:
            total_value_locked = CHAR_NULL

        # market cap
        try:
            prime, secon, terce = datos[7].find_all('span')
            market_cap = self.__fora_extras(prime.text, divisa_ref)
            market_cap_change_pctx = self.__mais_menos(terce)+secon.text
        except:
            market_cap = CHAR_NULL
            market_cap_change_pctx = CHAR_NULL
        # fully diluted market cap
        try:
            prime, secon, terce = datos[8].find_all('span')
            fully_diluted_market_cap = self.__fora_extras(prime.text, divisa_ref)
            fully_diluted_market_cap_change_pctx = self.__mais_menos(terce)+secon.text
        except:
            fully_diluted_market_cap = CHAR_NULL
            fully_diluted_market_cap_change_pctx = CHAR_NULL
        # min/max onte
        if datos[9].text != 'No Data':
            max_onte, min_onte = [ele.rstrip() for ele in self.__fora_extras(datos[9].text, divisa_ref).split('/')]
        else:
            max_onte = min_onte = CHAR_NULL
        # open/close onte
        if datos[10].text != 'No Data':
            onte_ini, onte_fin = [ele.rstrip() for ele in self.__fora_extras(datos[10].text, divisa_ref).split('/')]
        else:
            onte_ini = onte_fin = CHAR_NULL
        # cambio onte
        price_change_pctx_onte = datos[11].text
        if 'red' in str(datos[11]):
            price_change_pctx_onte = '+'+price_change_pctx_onte
        else:
            price_change_pctx_onte = '-'+price_change_pctx_onte
        # volume onte
        volume_onte = self.__fora_extras(datos[12].text, divisa_ref)
        # min/max 7d
        if datos[13].text != 'No Data':
            min_7d, max_7d = [ele.rstrip() for ele in self.__fora_extras(datos[13].text, divisa_ref).split('/')]
        else:
            min_7d = max_7d = CHAR_NULL
        # min/max 30d
        if datos[14].text != 'No Data':
            min_30d, max_30d = [ele.rstrip() for ele in self.__fora_extras(datos[14].text, divisa_ref).split('/')]
        else:
            min_30d = max_30d = CHAR_NULL
        # min/max 90d
        if datos[15].text != 'No Data':
            min_90d, max_90d = [ele.rstrip() for ele in self.__fora_extras(datos[15].text, divisa_ref).split('/')]
        else:
            min_90d = max_90d = CHAR_NULL
        # min/max 52semanas
        if datos[16].text != 'No Data':
            min_52semanas, max_52semanas = [ele.rstrip() for ele in self.__fora_extras(datos[16].text, divisa_ref).split('/')]
        else:
            min_52semanas = max_52semanas = CHAR_NULL
        # all time high
        try:
            prime, secon, terce = datos[17].find_all('span')
            ath = self.__fora_extras(prime.text, divisa_ref)
            ath_change_pctx = self.__mais_menos(terce)+secon.text
        except:
            ath = CHAR_NULL
            ath_change_pctx = CHAR_NULL
        # all time low
        try:
            prime, secon, terce = datos[18].find_all('span')
            atl = self.__fora_extras(prime.text, divisa_ref)
            atl_change_pctx = self.__mais_menos(terce)+secon.text
        except:
            atl = CHAR_NULL
            atl_change_pctx = CHAR_NULL
        # roi da moeda (comprado no momento da saída ou no primeiro momento rexistrado)
        roi = datos[19].text
        if roi != 'No Data':
            if 'green' in str(datos[19]):
                roi = '+'+roi
            else:
                roi = '-'+roi
        # circulating supply
        circulating_supply = datos[20].text
        if circulating_supply != 'No Data':
            circulating_supply = self.__fora_extras(circulating_supply.split(' ')[0])
        # total supply
        total_supply = datos[21].text
        if total_supply != 'No Data':
            total_supply = self.__fora_extras(total_supply.split(' ')[0])
        # max supply
        max_supply = datos[22].text
        if max_supply != 'No Data':
            max_supply = self.__fora_extras(max_supply.split(' ')[0])

        watchlists = self.__fora_extras(soup.find_all(class_='namePill')[2].text.split(' ')[1])

        dic = {
                'timestamp': str(datetime.now()),
                'rango': rango,
                'simbolo': obx_buscado[0],
                'nome': obx_buscado[1],
                'prezo': prezo,
                'divisa_ref': divisa_ref,
                'price_change_24h': price_change_24h,
                'price_change_pctx_24h': price_change_pctx_24h,
                'max_24h': max_24h,
                'min_24h': min_24h,
                'trading_volume_24h': trading_volume_24h,
                'trading_volume_change_pctx_24h': trading_volume_change_pctx_24h,
                'volume_dividido_market_cap': volume_dividido_market_cap,
                'dominancia_mercado': dominancia_mercado,
                'market_cap': market_cap,
                'market_cap_change_pctx': market_cap_change_pctx,
                'fully_diluted_market_cap': fully_diluted_market_cap,
                'fully_diluted_market_cap_change_pctx': fully_diluted_market_cap_change_pctx,
                'max_onte': max_onte,
                'min_onte': min_onte,
                'onte_ini': onte_ini,
                'onte_fin': onte_fin,
                'price_change_pctx_onte': price_change_pctx_onte,
                'volume_onte': volume_onte,
                'max_7d': max_7d,
                'min_7d': min_7d,
                'max_30d': max_30d,
                'min_30d': min_30d,
                'max_90d': max_90d,
                'min_90d': min_90d,
                'max_52semanas': max_52semanas,
                'min_52semanas': min_52semanas,
                'ath': ath,
                'ath_change_pctx': ath_change_pctx,
                'atl': atl,
                'atl_change_pctx': atl_change_pctx,
                'roi': roi,
                'circulating_supply': circulating_supply,
                'total_supply': total_supply,
                'max_supply': max_supply,
                'total_value_locked': total_value_locked,
                'watchlists': watchlists
                }

        for chave, valor in zip(dic.keys(), dic.values()):
            if (valor == '- -') or (valor == '') or (valor == '--') or (valor == 'No Data'):
                dic[chave] = CHAR_NULL
        return dic

# ------------------------------------------------------------------------------
