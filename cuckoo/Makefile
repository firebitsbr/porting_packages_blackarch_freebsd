PORTNAME=	cuckoo
DISTVERSION=	2.0.7
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Automated malware analysis system.
WWW=		http://cuckoosandbox.org/

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-pip@${PY_FLAVOR}

RUN_DEPENDS=	??/libvirt \
		??/py-alembic@${PY_FLAVOR} \
		??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-bottle@${PY_FLAVOR} \
		??/py-cffi@${PY_FLAVOR} \
		??/py-chardet@${PY_FLAVOR} \
		??/py-dateutil@${PY_FLAVOR} \
		??/py-django@${PY_FLAVOR} \
		??/py-dpkt@${PY_FLAVOR} \
		??/py-ecdsa@${PY_FLAVOR} \
		??/py-egghatch@${PY_FLAVOR} \
		??/py-enum34@${PY_FLAVOR} \
		??/py-flask-sqlalchemy@${PY_FLAVOR} \
		??/py-flask@${PY_FLAVOR} \
		??/py-gevent@${PY_FLAVOR} \
		??/py-httpreplay@${PY_FLAVOR} \
		??/py-idna@${PY_FLAVOR} \
		??/py-ipaddress@${PY_FLAVOR} \
		??/py-itsdangerous@${PY_FLAVOR} \
		??/py-jinja@${PY_FLAVOR} \
		??/py-magic@${PY_FLAVOR} \
		??/py-mako@${PY_FLAVOR} \
		??/py-markupsafe@${PY_FLAVOR} \
		??/py-ndg-httpsclient@${PY_FLAVOR} \
		??/py-peepdf@${PY_FLAVOR} \
		??/py-pefile@${PY_FLAVOR} \
		??/py-pyasn1@${PY_FLAVOR} \
		??/py-pycparser@${PY_FLAVOR} \
		??/py-pydeep@${PY_FLAVOR} \
		??/py-pymongo@${PY_FLAVOR} \
		??/py-pyopenssl@${PY_FLAVOR} \
		??/py-sflock@${PY_FLAVOR} \
		??/py-sqlalchemy@${PY_FLAVOR} \
		??/py-tlslite-ng@${PY_FLAVOR} \
		??/py-wakeonlan@${PY_FLAVOR} \
		??/py-werkzeug@${PY_FLAVOR} \
		??/py-wol@${PY_FLAVOR} \
		??/py-yara@${PY_FLAVOR} \
		??/tcpdump \
		??/yara \
		devel/py-six@${PY_FLAVOR} \
		lang/python3 \
		net/py-scapy@${PY_FLAVOR} \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
