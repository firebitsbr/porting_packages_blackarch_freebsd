PORTNAME=	v3n0m
DISTVERSION=	536.16b629f
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Offensive Security Tool for Vulnerability Scanning & Pentesting
WWW=		https://github.com/v3n0m-Scanner/V3n0M-Scanner

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-aiohttp@${PY_FLAVOR} \
		??/py-asyncio@${PY_FLAVOR} \
		??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-dnspython@${PY_FLAVOR} \
		??/py-fuzzywuzzy@${PY_FLAVOR} \
		??/py-httplib2@${PY_FLAVOR} \
		??/py-pyparsing@${PY_FLAVOR} \
		??/py-pysocks@${PY_FLAVOR} \
		??/py-socks@${PY_FLAVOR} \
		??/py-termcolor@${PY_FLAVOR} \
		??/py-tld@${PY_FLAVOR} \
		??/py-tqdm@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
