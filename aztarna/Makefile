PORTNAME=	aztarna
DISTVERSION=	1.2.1
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A footprinting tool for ROS and SROS systems.
WWW=		https://github.com/aliasrobotics/aztarna

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-aiohttp-xmlrpc@${PY_FLAVOR} \
		??/py-aiohttp@${PY_FLAVOR} \
		??/py-argcomplete@${PY_FLAVOR} \
		??/py-asn1crypto@${PY_FLAVOR} \
		??/py-async-timeout@${PY_FLAVOR} \
		??/py-attrs@${PY_FLAVOR} \
		??/py-babel@${PY_FLAVOR} \
		??/py-certifi@${PY_FLAVOR} \
		??/py-cffi@${PY_FLAVOR} \
		??/py-chardet@${PY_FLAVOR} \
		??/py-click-plugins@${PY_FLAVOR} \
		??/py-click@${PY_FLAVOR} \
		??/py-colorama@${PY_FLAVOR} \
		??/py-cryptography@${PY_FLAVOR} \
		??/py-dnspython@${PY_FLAVOR} \
		??/py-docutils@${PY_FLAVOR} \
		??/py-idna@${PY_FLAVOR} \
		??/py-idna_ssl@${PY_FLAVOR} \
		??/py-imagesize@${PY_FLAVOR} \
		??/py-ipwhois@${PY_FLAVOR} \
		??/py-jinja@${PY_FLAVOR} \
		??/py-lxml@${PY_FLAVOR} \
		??/py-markupsafe@${PY_FLAVOR} \
		??/py-multidict@${PY_FLAVOR} \
		??/py-packaging@${PY_FLAVOR} \
		??/py-property@${PY_FLAVOR} \
		??/py-pycparser@${PY_FLAVOR} \
		??/py-pygments@${PY_FLAVOR} \
		??/py-pyparsing@${PY_FLAVOR} \
		??/py-pytz@${PY_FLAVOR} \
		??/py-shodan@${PY_FLAVOR} \
		??/py-snowballstemmer@${PY_FLAVOR} \
		??/py-sphinx@${PY_FLAVOR} \
		??/py-sphinxcontrib-websupport@${PY_FLAVOR} \
		??/py-urllib3@${PY_FLAVOR} \
		??/py-uvloop@${PY_FLAVOR} \
		??/py-xlsxwriter@${PY_FLAVOR} \
		??/py-yarl@${PY_FLAVOR} \
		devel/py-six@${PY_FLAVOR} \
		lang/python \
		net/py-scapy@${PY_FLAVOR} \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
