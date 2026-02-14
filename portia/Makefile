PORTNAME=	portia
DISTVERSION=	39.2e6e608
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Automate a number of techniques commonly performed on internal network penetration tests after a low privileged account has been compromised.
WWW=		https://github.com/SpiderLabs/portia

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/ntdsxtract \
		??/py-argparse@${PY_FLAVOR} \
		??/py-dnspython@${PY_FLAVOR} \
		??/py-impacket@${PY_FLAVOR} \
		??/py-netaddr@${PY_FLAVOR} \
		??/py-nmap@${PY_FLAVOR} \
		??/py-pyasn1@${PY_FLAVOR} \
		??/py-pymysql@${PY_FLAVOR} \
		??/py-pyopenssl@${PY_FLAVOR} \
		??/py-pysmb@${PY_FLAVOR} \
		??/py-tabulate@${PY_FLAVOR} \
		??/py-termcolor@${PY_FLAVOR} \
		??/py-xmltodict@${PY_FLAVOR} \
		??/pymssql \
		??/volatility3 \
		devel/py-setuptools@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
