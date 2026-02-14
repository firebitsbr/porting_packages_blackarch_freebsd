PORTNAME=	pyadrecon
DISTVERSION=	0.6.3
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Gathers information about the Active Directory and generates a report which can provide a holistic picture of the current state of the target AD environment.
WWW=		https://github.com/l4rm4nd/PyADRecon

LICENSE=	GPLv3 # Defaulting to GPLv3


RUN_DEPENDS=	??/impacket \
		??/py-gssapi@${PY_FLAVOR} \
		??/py-ldap3@${PY_FLAVOR} \
		??/py-openpyxl@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
