PORTNAME=	nettacker
DISTVERSION=	0.4.0.r151.gdeb2742
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Automated Penetration Testing Framework.
WWW=		https://github.com/OWASP/Nettacker

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		??/py-installer@${PY_FLAVOR} \
		??/py-poetry@${PY_FLAVOR} \
		??/py-wheel@${PY_FLAVOR} \
		devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/canari \
		??/flake8 \
		??/py-aiohttp@${PY_FLAVOR} \
		??/py-backoff@${PY_FLAVOR} \
		??/py-bs4@${PY_FLAVOR} \
		??/py-censys@${PY_FLAVOR} \
		??/py-flask@${PY_FLAVOR} \
		??/py-ipaddr@${PY_FLAVOR} \
		??/py-lockfile@${PY_FLAVOR} \
		??/py-mechanize@${PY_FLAVOR} \
		??/py-multiprocess@${PY_FLAVOR} \
		??/py-netaddr@${PY_FLAVOR} \
		??/py-numpy@${PY_FLAVOR} \
		??/py-paramiko@${PY_FLAVOR} \
		??/py-psycopg2@${PY_FLAVOR} \
		??/py-py3dns@${PY_FLAVOR} \
		??/py-pycurl@${PY_FLAVOR} \
		??/py-pyopenssl@${PY_FLAVOR} \
		??/py-pysocks@${PY_FLAVOR} \
		??/py-pyspf@${PY_FLAVOR} \
		??/py-rule@${PY_FLAVOR} \
		??/py-shodan@${PY_FLAVOR} \
		??/py-sqlalchemy@${PY_FLAVOR} \
		??/py-terminable-thread@${PY_FLAVOR} \
		??/py-texttable@${PY_FLAVOR} \
		??/py-win_inet_pton@${PY_FLAVOR} \
		??/py-xmltodict@${PY_FLAVOR} \
		??/scapy \
		devel/py-six@${PY_FLAVOR} \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
