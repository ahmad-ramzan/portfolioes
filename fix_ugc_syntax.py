import re

ugcimages_clean = """            {
                id: 'ugcimages', label: 'UGC Image Design', h: 'UGC Product Image Design',
                groups: [
                    {
                        sub: 'Product Shot Designs', items: [
                            { t: 'UGC Product Image 1', u: 'https://drive.google.com/file/d/1NBxE50fviWGrlFSVkpBy37E2DjUWcT0c/view?usp=drive_link', img: 'https://drive.google.com/thumbnail?id=1NBxE50fviWGrlFSVkpBy37E2DjUWcT0c&sz=w640' },
                            { t: 'UGC Product Image 2', u: 'https://drive.google.com/file/d/11RS2YDeyi5QRSzEUbWpO4D9bUTpZk6Xa/view?usp=drive_link', img: 'https://drive.google.com/thumbnail?id=11RS2YDeyi5QRSzEUbWpO4D9bUTpZk6Xa&sz=w640' },
                            { t: 'UGC Product Image 3', u: 'https://drive.google.com/file/d/13NXNh3HTOZCjcKKsuQ_38CW59rGnSt1A/view?usp=drive_link', img: 'https://drive.google.com/thumbnail?id=13NXNh3HTOZCjcKKsuQ_38CW59rGnSt1A&sz=w640' },
                            { t: 'UGC Product Image 4', u: 'https://drive.google.com/file/d/1EISujruKwAokT_f6SZ749bTsVsmnclpA/view?usp=drive_link', img: 'https://drive.google.com/thumbnail?id=1EISujruKwAokT_f6SZ749bTsVsmnclpA&sz=w640' },
                            { t: 'UGC Product Image 5', u: 'https://drive.google.com/file/d/1k6otQHfS223rvLsXMgtGaMOnoHuT1f8W/view?usp=drive_link', img: 'https://drive.google.com/thumbnail?id=1k6otQHfS223rvLsXMgtGaMOnoHuT1f8W&sz=w640' },
                            { t: 'UGC Product Image 6', u: 'https://drive.google.com/file/d/1E9DXizg2drP1bnTeKECdCRup8mk61pOy/view?usp=drive_link', img: 'https://drive.google.com/thumbnail?id=1E9DXizg2drP1bnTeKECdCRup8mk61pOy&sz=w640' },
                            { t: 'UGC Product Image 7', u: 'https://drive.google.com/file/d/1h0zzn4_4EAgn0g6r-hQ_KgGgcqyBaxOi/view?usp=drive_link', img: 'https://drive.google.com/thumbnail?id=1h0zzn4_4EAgn0g6r-hQ_KgGgcqyBaxOi&sz=w640' }
                        ]
                    },
                    {
                        sub: 'Influencer UGC Ads', items: [
                            { t: 'Influencer UGC Image 1', u: 'https://drive.google.com/file/d/1aVlM4v2HM51649PwVNpuXFjKeN8B9Vni/view?usp=drive_link', img: 'https://drive.google.com/thumbnail?id=1aVlM4v2HM51649PwVNpuXFjKeN8B9Vni&sz=w640' },
                            { t: 'Influencer UGC Image 2', u: 'https://drive.google.com/file/d/16-IZoeNhi6BvbeMNGnVAWCdWDcfZT_iU/view?usp=drive_link', img: 'https://drive.google.com/thumbnail?id=16-IZoeNhi6BvbeMNGnVAWCdWDcfZT_iU&sz=w640' },
                            { t: 'Influencer UGC Image 3', u: 'https://drive.google.com/file/d/1lTlE9VE5JZdaqiBDufGvU-NpcVBNhLxs/view?usp=drive_link', img: 'https://drive.google.com/thumbnail?id=1lTlE9VE5JZdaqiBDufGvU-NpcVBNhLxs&sz=w640' },
                            { t: 'Influencer UGC Image 4', u: 'https://drive.google.com/file/d/1H87owFbyCllZ8tTE8If7B1hxg-5TrPyX/view?usp=drive_link', img: 'https://drive.google.com/thumbnail?id=1H87owFbyCllZ8tTE8If7B1hxg-5TrPyX&sz=w640' },
                            { t: 'Influencer UGC Image 5', u: 'https://drive.google.com/file/d/11-v23YT_NPjEzkkf_6vLibo0bRayV1yW/view?usp=drive_link', img: 'https://drive.google.com/thumbnail?id=11-v23YT_NPjEzkkf_6vLibo0bRayV1yW&sz=w640' },
                            { t: 'Influencer UGC Image 6', u: 'https://drive.google.com/file/d/1fHAbwGSmOQNAo_XYVRH7VvgOOvnr9UKW/view?usp=drive_link', img: 'https://drive.google.com/thumbnail?id=1fHAbwGSmOQNAo_XYVRH7VvgOOvnr9UKW&sz=w640' },
                            { t: 'Influencer UGC Image 7', u: 'https://drive.google.com/file/d/1TA79gz3gBjO27vQhT0J1q4DwB1XoizPF/view?usp=drive_link', img: 'https://drive.google.com/thumbnail?id=1TA79gz3gBjO27vQhT0J1q4DwB1XoizPF&sz=w640' }
                        ]
                    },
                    {
                        sub: 'Influencer Style Concepts', items: [
                            { t: 'UGC Influencer Image 1', u: 'https://drive.google.com/file/d/1n88T9Am3cTVIr_mLBxJ8AvmmQIu9Rsxm/view?usp=drive_link', img: 'https://drive.google.com/thumbnail?id=1n88T9Am3cTVIr_mLBxJ8AvmmQIu9Rsxm&sz=w640' },
                            { t: 'UGC Influencer Image 2', u: 'https://drive.google.com/file/d/150NHRU2baeC5S9sXHoTCwMQDVnvZXrZH/view?usp=drive_link', img: 'https://drive.google.com/thumbnail?id=150NHRU2baeC5S9sXHoTCwMQDVnvZXrZH&sz=w640' },
                            { t: 'UGC Influencer Image 3', u: 'https://drive.google.com/file/d/1gET3doUiQo6boBTcF56z--LHTBpZibwG/view?usp=drive_link', img: 'https://drive.google.com/thumbnail?id=1gET3doUiQo6boBTcF56z--LHTBpZibwG&sz=w640' },
                            { t: 'UGC Influencer Image 4', u: 'https://drive.google.com/file/d/1khEsRE84XJTF8Mll4GCpGoZA0DrU8LRw/view?usp=drive_link', img: 'https://drive.google.com/thumbnail?id=1khEsRE84XJTF8Mll4GCpGoZA0DrU8LRw&sz=w640' },
                            { t: 'UGC Influencer Image 5', u: 'https://drive.google.com/file/d/11MkvIc_Zuf6PXVpBk-X4YM6R9Nhoh7fo/view?usp=drive_link', img: 'https://drive.google.com/thumbnail?id=11MkvIc_Zuf6PXVpBk-X4YM6R9Nhoh7fo&sz=w640' },
                            { t: 'UGC Influencer — Design Concept', u: 'https://drive.google.com/file/d/1F_fqrbNlNHdPcWg_sRc0EUFGti6uiQnm/view?usp=drive_link', img: 'https://drive.google.com/thumbnail?id=1F_fqrbNlNHdPcWg_sRc0EUFGti6uiQnm&sz=w640' }
                        ]
                    },
                    {
                        sub: 'Lifestyle & Social UGC', items: [
                            { t: 'Influencer Image 1', u: 'https://drive.google.com/file/d/10OP-v1BOosR9XHke8WL3dq_dzFcgrsgd/view?usp=drive_link', img: 'https://drive.google.com/thumbnail?id=10OP-v1BOosR9XHke8WL3dq_dzFcgrsgd&sz=w640' },
                            { t: 'Influencer Image 2', u: 'https://drive.google.com/file/d/1SAPHE020qOAfDzBTxaa20spCU5gnb2P3/view?usp=drive_link', img: 'https://drive.google.com/thumbnail?id=1SAPHE020qOAfDzBTxaa20spCU5gnb2P3&sz=w640' },
                            { t: 'Influencer Image 3', u: 'https://drive.google.com/file/d/1_PAdvfxRHq3XZsmIz4uBHO-ar8pulrbA/view?usp=drive_link', img: 'https://drive.google.com/thumbnail?id=1_PAdvfxRHq3XZsmIz4uBHO-ar8pulrbA&sz=w640' },
                            { t: 'Influencer Video 1', u: 'https://drive.google.com/file/d/1HIRSOI-WVXIJC8y1Uc0XwXEut_WlEbPw/view?usp=drive_link', img: 'https://drive.google.com/thumbnail?id=1HIRSOI-WVXIJC8y1Uc0XwXEut_WlEbPw&sz=w640' },
                            { t: 'Influencer Video 2', u: 'https://drive.google.com/file/d/19C06aUXBKnLOwPC2QeV1Xq3VPJYKuJ1m/view?usp=drive_link', img: 'https://drive.google.com/thumbnail?id=19C06aUXBKnLOwPC2QeV1Xq3VPJYKuJ1m&sz=w640' }
                        ]
                    },
                    {
                        sub: 'Fashion & Outfit Prompts', items: [
                            { t: 'Fashion UGC Image 1', u: 'https://drive.google.com/file/d/1j9VoFjqXdh7XNMFEhCbd5l_IYcvNjuAK/view?usp=drive_link', img: 'https://drive.google.com/thumbnail?id=1j9VoFjqXdh7XNMFEhCbd5l_IYcvNjuAK&sz=w640' },
                            { t: 'Fashion UGC Image 2', u: 'https://drive.google.com/file/d/1454vPVEfw61mAfAemvsJ1SvNYN2RAjI3/view?usp=drive_link', img: 'https://drive.google.com/thumbnail?id=1454vPVEfw61mAfAemvsJ1SvNYN2RAjI3&sz=w640' },
                            { t: 'Fashion UGC Image 3', u: 'https://drive.google.com/file/d/1j0ku3O5tDFXtUxUMHoFZ-LGmC0antS9V/view?usp=drive_link', img: 'https://drive.google.com/thumbnail?id=1j0ku3O5tDFXtUxUMHoFZ-LGmC0antS9V&sz=w640' },
                            { t: 'Fashion UGC Image 4', u: 'https://drive.google.com/file/d/1ijYcw2Th9azn4rtH6l6G5FktuJ3Vfqyn/view?usp=drive_link', img: 'https://drive.google.com/thumbnail?id=1ijYcw2Th9azn4rtH6l6G5FktuJ3Vfqyn&sz=w640' },
                            { t: 'Fashion UGC Image 5', u: 'https://drive.google.com/file/d/1qyCip8aDj2O-7gQ46Dtv5wn0IPskx0BM/view?usp=drive_link', img: 'https://drive.google.com/thumbnail?id=1qyCip8aDj2O-7gQ46Dtv5wn0IPskx0BM&sz=w640' },
                            { t: 'Fashion UGC Image 6', u: 'https://drive.google.com/file/d/1jNRQNkuij-PEqFbWoQ2gQnwCrZC_i5yk/view?usp=drive_link', img: 'https://drive.google.com/thumbnail?id=1jNRQNkuij-PEqFbWoQ2gQnwCrZC_i5yk&sz=w640' }
                        ]
                    },
                    {
                        sub: 'AI UGC Actors & Characters', items: [
                            { t: 'AI UGC Actor 1', u: 'https://drive.google.com/file/d/1LeSCSUSo9glslgSIC_7eS5IvuguXqyCb/view?usp=drive_link', img: 'https://drive.google.com/thumbnail?id=1LeSCSUSo9glslgSIC_7eS5IvuguXqyCb&sz=w640' },
                            { t: 'AI UGC Actor 2', u: 'https://drive.google.com/file/d/1Kmj6bOzpsWVjsbWSG2zbZqu1y3l2IjWc/view?usp=drive_link', img: 'https://drive.google.com/thumbnail?id=1Kmj6bOzpsWVjsbWSG2zbZqu1y3l2IjWc&sz=w640' },
                            { t: 'AI UGC Actor 3', u: 'https://drive.google.com/file/d/1lCjDdqmXQEWUxKNvxQ6B8AclC6VtgnIC/view?usp=drive_link', img: 'https://drive.google.com/thumbnail?id=1lCjDdqmXQEWUxKNvxQ6B8AclC6VtgnIC&sz=w640' },
                            { t: 'AI UGC Actor 4', u: 'https://drive.google.com/file/d/1uXtfN2VrP55k9_He7ZSyviVnOK6E95vR/view?usp=drive_link', img: 'https://drive.google.com/thumbnail?id=1uXtfN2VrP55k9_He7ZSyviVnOK6E95vR&sz=w640' },
                            { t: 'AI UGC Actor 5', u: 'https://drive.google.com/file/d/1bNwGEJjn6ugwFGwIo16roIGSybmpMq3m/view?usp=drive_link', img: 'https://drive.google.com/thumbnail?id=1bNwGEJjn6ugwFGwIo16roIGSybmpMq3m&sz=w640' },
                            { t: 'AI UGC Actor 6', u: 'https://drive.google.com/file/d/1X-_DvP9SXATsTQjkeSR1wDm-JcIOmIDh/view?usp=drive_link', img: 'https://drive.google.com/thumbnail?id=1X-_DvP9SXATsTQjkeSR1wDm-JcIOmIDh&sz=w640' }
                        ]
                    }
                ]
            },"""

with open(r'c:\Users\Ch Asad Waqas Kamboh\portfolioes\other-projects.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the ugcimages block completely
html = re.sub(r"\s*\{\s*id:\s*'ugcimages'.*?\}\s*,\s*\{\s*id:\s*'animations20'", "\n" + ugcimages_clean + "\n            {\n                id: 'animations20'", html, flags=re.DOTALL)

with open(r'c:\Users\Ch Asad Waqas Kamboh\portfolioes\other-projects.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("ugcimages section cleaned up perfectly!")
