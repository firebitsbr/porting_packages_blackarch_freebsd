PORTNAME=	responder
DISTVERSION=	v3.2.2.0.r0.gfb29fe2
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A LLMNR and NBT-NS poisoner, with built-in HTTP/SMB/MSSQL/FTP/LDAP rogue authentication server supporting NTLMv1/NTLMv2/LMv2 (multirelay version).
WWW=		https://github.com/lgandx/Responder

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/impacket \
		??/mingw-w64-gcc \
		??/py-aioquic@${PY_FLAVOR} \
		??/py-cryptography@${PY_FLAVOR} \
		??/py-netifaces@${PY_FLAVOR} \
		??/py-pycryptodome@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
