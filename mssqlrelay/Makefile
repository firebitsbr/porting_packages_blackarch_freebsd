PORTNAME=	mssqlrelay
DISTVERSION=	11.bd764b9
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Microsoft SQL Relay is an offensive tool for auditing and abusing Microsoft SQL (MSSQL) services.
WWW=		https://github.com/CompassSecurity/mssqlrelay

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/impacket-ba \
		??/py-asn1crypto@${PY_FLAVOR} \
		??/py-cryptography@${PY_FLAVOR} \
		??/py-dnspython@${PY_FLAVOR} \
		??/py-dsinternals@${PY_FLAVOR} \
		??/py-ldap3@${PY_FLAVOR} \
		??/py-pyasn1@${PY_FLAVOR} \
		??/py-pyopenssl@${PY_FLAVOR} \
		??/py-requests-ntlm@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
