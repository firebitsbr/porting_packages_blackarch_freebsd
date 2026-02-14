PORTNAME=	patator
DISTVERSION=	1.1.0.r4.g964e87c
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A multi-purpose bruteforcer.
WWW=		https://github.com/lanjelot/patator

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		devel/git \
		devel/py-pip@${PY_FLAVOR}

RUN_DEPENDS=	??/ike-scan \
		??/impacket \
		??/java-environment \
		??/mysql-python \
		??/openldap \
		??/py-ajpy@${PY_FLAVOR} \
		??/py-cx_oracle@${PY_FLAVOR} \
		??/py-dnspython@${PY_FLAVOR} \
		??/py-ipy@${PY_FLAVOR} \
		??/py-paramiko@${PY_FLAVOR} \
		??/py-psycopg2@${PY_FLAVOR} \
		??/py-pyasn1@${PY_FLAVOR} \
		??/py-pycryptodome@${PY_FLAVOR} \
		??/py-pycurl@${PY_FLAVOR} \
		??/py-pyopenssl@${PY_FLAVOR} \
		??/py-pysnmp@${PY_FLAVOR} \
		archivers/unzip \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
